import os
import faiss
import numpy as np
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from pathlib import Path

# --- Utils functions ---
from .utils.get_files_paths import get_files_paths
from .utils.build_tree_from_md import build_tree_from_md
from .utils.delete_file import delete_single_file

# --- Constants ---
from . import myconstants

# --- Controller functions ---
from controllers import file as file_controller
from controllers import default_chunk as default_chunk_controller
from controllers import smart_chunk as smart_chunk_controller

# Load the environment variables
load_dotenv()
try:
    api_key = os.getenv("API_KEY")
except KeyError:
    print("Error: API_KEY environment variable not set.", flush=True)

genai.configure(api_key=api_key)

gemini_model = genai.GenerativeModel('gemini-1.5-flash-latest')

class Vector_db():
    def __init__(self, embeddingDimension=768):
        self.embedding_dim = embeddingDimension
        self.unprocessed_files_folder_path = myconstants.UNPROCESSED_FILES_DIR
        self.modify_files_folder_path = myconstants.MODIFY_FILES_DIR
        self.files = {}
        self.default_chunks = {}
        self.smart_chunks = {}

        # In-memory caches of the actual chunk objects
        self.vector_db_smart_embeddings = faiss.IndexFlatL2(embeddingDimension)
        self.vector_db_default_embeddings = faiss.IndexFlatL2(embeddingDimension)

        # Mappings from session ID (FAISS index) to permanent ID (Mongo ObjectId)
        self.faiss_id_to_smart_chunk_id: dict[int, str] = {}
        self.faiss_id_to_default_chunk_id: dict[int, str] = {}

        # Reverse mappings from Mongo ObjectId to FAISS index
        self.mongo_id_to_smart_faiss_id: dict[str, int] = {}
        self.mongo_id_to_default_faiss_id: dict[str, int] = {}

        # Sets to track soft-deleted FAISS IDs
        self.deleted_default_faiss_ids = set()
        self.deleted_smart_faiss_ids = set()

    @classmethod
    async def create(cls, embeddingDimension=768):
        """Asynchronously creates and initializes an instance of Vector_db."""
        instance = cls(embeddingDimension)
        await instance._load_db_data()
        await instance._startup_files_processing()
        return instance
    
    async def _load_db_data(self):
        """
        Asynchronously loads data from MongoDB (the source of truth) and correctly
        rebuilds the temporary in-memory FAISS indexes and their mappings.
        """
        print("Loading data from database and rebuilding FAISS indexes...", flush=True)
        files_from_db = await file_controller.get_all_files()
        self.files = {f.filename: f for f in files_from_db}

        # Default chunks
        default_chunks_from_db = await default_chunk_controller.get_all_chunks()
        if default_chunks_from_db:
            # Create a stable sort order based on the permanent MongoDB ID
            sorted_chunks = sorted(default_chunks_from_db, key=lambda c: c.id)
            
            # Rebuild the FAISS index from scratch
            embeddings_to_load = np.array([c.embedding for c in sorted_chunks], dtype=np.float32)
            self.vector_db_default_embeddings.add(embeddings_to_load)

            # Rebuild the in-memory map and cache
            for i, chunk in enumerate(sorted_chunks):
                self.faiss_id_to_default_chunk_id[i] = str(chunk.id)
                self.mongo_id_to_default_faiss_id[str(chunk.id)] = i
                self.default_chunks[str(chunk.id)] = chunk

        # Smart chunks
        smart_chunks_from_db = await smart_chunk_controller.get_all_chunks()
        if smart_chunks_from_db:
            sorted_chunks = sorted(smart_chunks_from_db, key=lambda c: c.id)
            embeddings_to_load = np.array([c.embedding for c in sorted_chunks], dtype=np.float32)
            self.vector_db_smart_embeddings.add(embeddings_to_load)

            for i, chunk in enumerate(sorted_chunks):
                self.faiss_id_to_smart_chunk_id[i] = str(chunk.id)
                self.mongo_id_to_smart_faiss_id[str(chunk.id)] = i
                self.smart_chunks[str(chunk.id)] = chunk
        
        print(f"Loaded {len(self.files)} files. Rebuilt FAISS indexes: {self.vector_db_default_embeddings.ntotal} default chunks, {self.vector_db_smart_embeddings.ntotal} smart chunks.", flush=True)

    async def _startup_files_processing(self):
        """Asynchronously process any files in the unprocessed folder on startup."""
        if not os.path.isdir(self.unprocessed_files_folder_path):
            raise FileNotFoundError(f"Directory for unprocessed files not found: {self.unprocessed_files_folder_path}")
        
        unprocessed_files_paths = get_files_paths(self.unprocessed_files_folder_path)

        # Filter files that were already added before
        files_to_delete = [path for path in unprocessed_files_paths if path in self.files]
        if files_to_delete:
            print(f"Found {len(files_to_delete)} already processed files. Deleting them from source.", flush=True)

            root = Path(self.unprocessed_files_folder_path).resolve()
            for path in files_to_delete:
                full_path = root / path
                delete_single_file(full_path)

        # Filter the files to process
        files_to_process = [path for path in unprocessed_files_paths if path not in self.files]
        if files_to_process:
            print(f"Found {len(files_to_process)} new files to process.", flush=True)
            tasks = [self.process_file(f_path) for f_path in files_to_process]
            await asyncio.gather(*tasks)
        else:
            print("No new files to process.", flush=True)
        
        # Check for files to be updated
        files_to_modify = get_files_paths(self.modify_files_folder_path)
        if files_to_modify:
            print(f"Found {len(files_to_modify)} new files to update.", flush=True)
            tasks = [self.process_file(f_path, update=True) for f_path in files_to_modify]
            await asyncio.gather(*tasks)
        else:
            print("No new files to update.", flush=True)

    async def process_file(self, path: str, update: bool = False):
        """Builds tree, generates embeddings, and saves everything to databases."""

        # Get the relative path of the file
        full_path_obj = Path(path)
        filename = full_path_obj.name
        parent_folder = full_path_obj.parent.name
        rel_path = f"/{parent_folder}/{filename}/"

        if update:
            print("Deleting the information of the previous version of the file...", flush=True)
            await self.delete_file_from_server(rel_path)
            print(f"Processing the updated version: {path}", flush=True)
        else:
            print(f"Processing file: {path}", flush=True)

        # Generate the default embeddings
        default_embeddings, delimiters = self._generate_embeddings_default(path)

        # Add the embeddings to the vector database
        default_chunk_mongo_ids = []
        for emb, delimiter in zip(default_embeddings, delimiters):
            vector = np.array([emb], dtype=np.float32)
            self.vector_db_default_embeddings.add(vector)

            faiss_id = self.vector_db_default_embeddings.ntotal - 1

            new_chunk_data = {
                "embedding": emb,
                "file_id": rel_path,
                "start_pos": delimiter[0],
                "end_pos": delimiter[1]
            }
            # Add to the database
            created_chunk = await default_chunk_controller.create_chunk(new_chunk_data)
            mongo_id = str(created_chunk.id)

            # Update mappings and caches
            self.faiss_id_to_default_chunk_id[faiss_id] = mongo_id
            self.faiss_id_to_default_chunk_id[mongo_id] = faiss_id
            self.default_chunks[mongo_id] = created_chunk
            default_chunk_mongo_ids.append(mongo_id)

        # Produce the smart embeddings
        el_tree = build_tree_from_md(path)
        smart_embeddings, nodes_processing_sequence = self._generate_smart_embeddings_from_tree(el_tree)

        # Add the embeddings to the vector database and save chunk info
        smart_chunk_mongo_ids = []
        for emb, node in zip(smart_embeddings, nodes_processing_sequence):
            vector = np.array([emb], dtype=np.float32)
            self.vector_db_smart_embeddings.add(vector)
            
            faiss_id = self.vector_db_smart_embeddings.ntotal - 1
            
            new_chunk_data = {
                "embedding": emb,
                "file_id": rel_path,
                "start_pos": node["start_pos"],
                "end_pos": node["end_pos"]
            }
            # Add to the database
            created_chunk = await smart_chunk_controller.create_chunk(new_chunk_data)
            mongo_id = str(created_chunk.id)

            # Update mappings and caches
            self.faiss_id_to_smart_chunk_id[faiss_id] = mongo_id
            self.mongo_id_to_smart_faiss_id[mongo_id] = faiss_id
            self.smart_chunks[mongo_id] = created_chunk
            smart_chunk_mongo_ids.append(mongo_id)
        
        summary = self._generate_summary(full_path_obj)

        # Store the file info in MongoDB
        new_file_data = {
            "filename": rel_path,
            "summary": summary,
            "chunks_ids_default_parsing": default_chunk_mongo_ids,
            "chunks_ids_smart_parsing": smart_chunk_mongo_ids
        }
        print(new_file_data, flush=True)
        # Await the async database operation
        created_file = await file_controller.create_file(new_file_data)
        self.files[rel_path] = created_file
        print(f"Finished processing {path}. Added {len(smart_embeddings)} smart chunks and {len(default_embeddings)} default chunks.", flush=True)

        # Delete file from the unprocessed files dir
        delete_single_file(path)

    def _generate_embeddings_default(self, path: str) -> tuple[list[list[float]], list[tuple[int, int]]]:
        """
        Produce the default embeddings using standard LangChain chunking and their character offsets.
        """
        loader = TextLoader(path, encoding="utf-8")
        documents = loader.load()

        if not documents or not documents[0].page_content:
            return [], []

        full_text = documents[0].page_content
        string_chunks = self._split_text_in_chunks(full_text)

        if not string_chunks:
            return [], []

        # Correctly calculate the start and end position of each chunk
        delimiters = []
        current_pos = 0
        for chunk in string_chunks:
            # Find the start position of the chunk in the original text
            start_pos = full_text.find(chunk, current_pos)
            if start_pos == -1:
                # This could happen with complex overlaps, try a safe fallback
                search_from = max(0, current_pos - 50) # 50 is the overlap size
                start_pos = full_text.find(chunk, search_from)
                if start_pos == -1:
                    delimiters.append((None, None))
                    continue # Could not find this chunk, skip it.

            end_pos = start_pos + len(chunk)
            delimiters.append((start_pos, end_pos))
            current_pos = start_pos + 1
        
        # Generate the embeddings
        try:
            result = genai.embed_content(
                model="models/text-embedding-004",
                content=string_chunks,
                task_type="RETRIEVAL_DOCUMENT"
            )
            return result['embedding'], delimiters
        except Exception as e:
            print(f"Error getting default embeddings for {path}. Error: {e}", flush=True)
            return [], []

    def _document_to_chunks(self, documents: list) -> list:
        """Splits LangChain documents into smaller chunks."""
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        return text_splitter.split_documents(documents)

    def _split_text_in_chunks(self, text: str) -> list[str]:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        return text_splitter.split_text(text)

    def _get_embeddings(self, text: str, split_in_chunks: bool = True) -> list[list[float]]:
        """
        Sends text to Gemini to get embeddings.
        Handles both chunked documents and single query strings.
        """
        if not text.strip():
            return []
        
        # If not splitting, the text itself is the content. Otherwise, chunk it.
        content_to_embed = self._split_text_in_chunks(text) if split_in_chunks else [text]
        
        if not content_to_embed:
            return []

        try:
            # Use RETRIEVAL_QUERY for search queries and RETRIEVAL_DOCUMENT for documents.
            task_type = "RETRIEVAL_QUERY" if not split_in_chunks else "RETRIEVAL_DOCUMENT"
            
            result = genai.embed_content(
                model="models/text-embedding-004",
                content=content_to_embed,
                task_type=task_type
            )
            return result['embedding']
        except Exception as e:
            print(f"Error getting embedding for text snippet: '{text[:50]}...'. Error: {e}", flush=True)
            return []

    def _generate_smart_embeddings_from_tree_aux(self, node: dict) -> tuple[list[list[float]], str, list[dict]]:
        """
        Aux function for the _generate_embeddings_from_tree so it performs recursively.
        """
        embeddings = []
        node_processed_order = []

        content = node["content"]
        new_embeddings = self._get_embeddings(content)
        embeddings.extend(new_embeddings)
        node_processed_order.extend([node] * len(new_embeddings))

        # Check if we reached a leaf
        if "children" not in node or not node["children"]:
            return embeddings, content, node_processed_order
    
        # Process the children
        child_content_list = [content]
        for child in node["children"]:
            child_embeddings, child_cumulative_content, child_nodes_processed = self._generate_smart_embeddings_from_tree_aux(child)
            embeddings.extend(child_embeddings)
            child_content_list.append(child_cumulative_content)
            node_processed_order.extend(child_nodes_processed)
        
        # Perform the comulative embedding generation
        cumulative_content = "\n".join(child_content_list)
        if cumulative_content != content:
            cumulative_embeddings = self._get_embeddings(cumulative_content)
            embeddings.extend(cumulative_embeddings)
            node_processed_order.extend([node] * len(cumulative_embeddings))

        return embeddings, cumulative_content, node_processed_order
        
    
    def _generate_smart_embeddings_from_tree(self, el_tree: list) -> list[list[float]]:
        """
        Generate the embeddings for the contents of the file in  bottom up approach,
        concatenating the contents of the children elements to the parents contents.
        """
        all_embeddings = []
        nodes_processing_sequence = []
        for root in el_tree:
            embeddings_from_root, _, nodes_processing_sequence_aux = self._generate_smart_embeddings_from_tree_aux(root)
            all_embeddings.extend(embeddings_from_root)
            nodes_processing_sequence.extend(nodes_processing_sequence_aux)
            
        return all_embeddings, nodes_processing_sequence

    async def delete_file_from_server(self, path: str) -> bool:
        print(f"Attempting to delete file and associated data for: {path}", flush=True)
        file_to_delete = self.files.pop(path, None)
        if not file_to_delete:
            print(f"File not found in memory cache: {path}. Checking database.", flush=True)
            file_to_delete = await file_controller.get_file_by_filename(path)
            if not file_to_delete:
                print(f"File not found in database: {path}. Nothing to delete.", flush=True)
                return False

        # Delete Default Chunks
        for chunk_mongo_id in file_to_delete.chunks_ids_default_parsing:

            # Delete from Default Chunks
            faiss_id = self.mongo_id_to_default_faiss_id.pop(chunk_mongo_id, None)
            if faiss_id is not None:
                self.deleted_default_faiss_ids.add(faiss_id)
                self.faiss_id_to_default_chunk_id.pop(faiss_id, None)
            self.default_chunks.pop(chunk_mongo_id, None)
            await default_chunk_controller.delete_chunk(chunk_mongo_id)

        # Delete from Smart Chunks
        for chunk_mongo_id in file_to_delete.chunks_ids_smart_parsing:
            faiss_id = self.mongo_id_to_smart_faiss_id.pop(chunk_mongo_id, None)
            if faiss_id is not None:
                self.deleted_smart_faiss_ids.add(faiss_id)
                self.faiss_id_to_smart_chunk_id.pop(faiss_id, None)
            self.smart_chunks.pop(chunk_mongo_id, None)
            await smart_chunk_controller.delete_chunk(chunk_mongo_id)
        
        # Delete the File document itself
        await file_controller.delete_file(file_to_delete.id)
        print(f"Successfully deleted file and cleaned up associated chunks for: {path}", flush=True)
        
        return True
    
    def _retrieve_ids_from_db(self, query: str, db, retrieve_limit: int = 10):

        query_embedding_list = self._get_embeddings(query, split_in_chunks=False)
        if not query_embedding_list:
            return [], 0
        
        vector = np.array([query_embedding_list[0]], dtype=np.float32)
        
        if db.ntotal == 0:
            return [], 0
        
        # To ensure we get `retrieve_limit` unique *documents*, we search for more *chunks*.
        # A safe heuristic is to search for a multiple of the limit, or all chunks if the total is less.
        # This gives us a ranked list of chunks to iterate through.
        k_to_search = min(db.ntotal, retrieve_limit * 15)

        distances, faiss_ids = db.search(vector, k_to_search)

        return distances, faiss_ids
    
    def get_relevant_docs_paths(self, query: str, retrieve_limit: int = 10, smart_chunking: bool = False) -> tuple[list[str], int]:
        """
        Searches for relevant documents based on a query and returns their paths.
        """

        # Select the correct database and mappings based on the search type
        if not smart_chunking:
            db = self.vector_db_default_embeddings
            id_map = self.faiss_id_to_default_chunk_id
            chunk_cache = self.default_chunks
        else:
            db = self.vector_db_smart_embeddings
            id_map = self.faiss_id_to_smart_chunk_id
            chunk_cache = self.smart_chunks

        distances, faiss_ids = self._retrieve_ids_from_db(query, db, retrieve_limit)

        if faiss_ids is None:
            return [], 0

        # Use a set to store unique document paths
        relevant_paths = set()

        # Iterate through the sorted chunk results until we have enough unique documents
        for faiss_id in faiss_ids[0]:
            if faiss_id == -1:  # FAISS returns -1 when no more results are found
                break
            
            mongo_id = id_map.get(faiss_id)
            if mongo_id:
                chunk = chunk_cache.get(mongo_id)
                if chunk:
                    relevant_paths.add(chunk.file_id)
                    # Check if we have reached the desired number of unique documents
                    if len(relevant_paths) >= retrieve_limit:
                        break  # Stop iterating once we have enough documents
        
        final_paths = list(relevant_paths)
        return final_paths, len(final_paths)
    
    def get_relevant_chunks(self, query: str, retrieve_limit: int = 10, smart_chunking: bool = False) -> tuple[list[dict], int]:
        """
        Searches for relevant document chunks based on a query. It returns a list of
        non-overlapping chunks, prioritizing larger chunks over smaller ones that are
        contained within them.
        """
        if not smart_chunking:
            db = self.vector_db_default_embeddings
            id_map = self.faiss_id_to_default_chunk_id
            chunk_cache = self.default_chunks
        else:
            db = self.vector_db_smart_embeddings
            id_map = self.faiss_id_to_smart_chunk_id
            chunk_cache = self.smart_chunks

        distances, faiss_ids = self._retrieve_ids_from_db(query, db, retrieve_limit)

        if faiss_ids is None:
            return [], 0
        
        relevant_chunks = []
        covered_areas = {} 

        for faiss_id in faiss_ids[0]:
            if faiss_id == -1:
                break
            
            mongo_id = id_map.get(faiss_id)
            if not mongo_id:
                continue
            
            chunk = chunk_cache.get(mongo_id)
            if not chunk or chunk.start_pos is None or chunk.end_pos is None:
                continue

            file_path = chunk.file_id
            start_pos = chunk.start_pos
            end_pos = chunk.end_pos

            is_contained = False
            if file_path in covered_areas:
                for area_start, area_end in covered_areas[file_path]:
                    if start_pos >= area_start and end_pos <= area_end:
                        is_contained = True
                        break
            
            if not is_contained:
                relevant_chunks.append({
                    "path": file_path,
                    "start_pos": start_pos,
                    "end_pos": end_pos
                })
                if file_path not in covered_areas:
                    covered_areas[file_path] = []
                covered_areas[file_path].append((start_pos, end_pos))

                if len(relevant_chunks) >= retrieve_limit:
                    break
        
        return relevant_chunks, len(relevant_chunks)
    
    def _generate_summary(self, file_path: str) -> str | None:
        """
        Uses the Gemini API to generate a concise summary for a document.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                full_text = f.read()
        except Exception as e:
            print(f"Error reading file {file_path} for summary: {e}", flush=True)
            return None

        if not full_text.strip():
            return None

        prompt = (
            "Generate a single, concise sentence that summarizes the document type, "
            "main topic, and overall purpose of the following text. Focus on high-level "
            "context, not specific details. Example: 'This document is a technical specification "
            "for the Apollo-11 guidance system, detailing its hardware components and software logic.'\n\n"
            f"TEXT: '''{full_text[:4000]}'''"
        )

        try:
            # --- BUG FIX: Use the modern 'GenerativeModel' and 'generate_content' method ---
            response = gemini_model.generate_content(prompt)
            # The response object has a 'text' attribute with the generated string
            summary = response.text.strip()
            print(f"Generated summary: {summary}", flush=True)
            return summary
        except Exception as e:
            print(f"Error generating summary: {e}", flush=True)
            return None