import os
import faiss
import numpy as np
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter

# --- Utils functions ---
from .utils.get_files_paths import get_files_paths
from .utils.build_tree_from_md import build_tree_from_md

# --- Constants ---
from . import myconstants

# --- Controller functions ---
from controllers import file as file_controller
from controllers import chunk as chunk_controller

# Load the environment variables
load_dotenv()
try:
    api_key = os.getenv("API_KEY")
except KeyError:
    print("Error: API_KEY environment variable not set.", flush=True)

genai.configure(api_key=api_key)

class Vector_db():
    def __init__(self, embeddingDimension=768):
        self.embedding_dim = embeddingDimension
        self.unprocessed_files_folder_path = myconstants.UNPROCESSED_FILES_DIR
        self.files = {}
        self.chunks = {}
        self.vector_db = faiss.IndexFlatL2(embeddingDimension)

    @classmethod
    async def create(cls, embeddingDimension=768):
        """Asynchronously creates and initializes an instance of Vector_db."""
        instance = cls(embeddingDimension)
        await instance._load_db_data()
        await instance._startup_files_processing()
        return instance
    
    async def _load_db_data(self):
        """Asynchronously loads existing data from MongoDB into memory."""
        print("Loading data from database...", flush=True)
        files_from_db = await file_controller.get_all_files()
        self.files = {f.id: f for f in files_from_db}

        chunks_from_db = await chunk_controller.get_all_chunks()
        self.chunks = {c.vector_db_id: c for c in chunks_from_db}

        if self.chunks:
            # Ensure order, because FAISS IDs are sequential from 0
            sorted_chunks = sorted(self.chunks.values(), key=lambda c: c.vector_db_id)
            embeddings_to_load = np.array([c.embedding for c in sorted_chunks], dtype=np.float32)
            self.vector_db.add(embeddings_to_load)
        
        print(f"Loaded {len(self.files)} files and {len(self.chunks)} chunks. FAISS index size: {self.vector_db.ntotal}", flush=True)

    async def _startup_files_processing(self):
        """Asynchronously process any files in the unprocessed folder on startup."""
        if not os.path.isdir(self.unprocessed_files_folder_path):
            raise FileNotFoundError(f"Directory for unprocessed files not found: {self.unprocessed_files_folder_path}")
        
        unprocessed_files_paths = get_files_paths(self.unprocessed_files_folder_path)
        
        # Create a list of async tasks to run concurrently
        tasks = [self.process_file(f_path) for f_path in unprocessed_files_paths]
        await asyncio.gather(*tasks)

    async def process_file(self, path: str):
        """Builds tree, generates embeddings, and saves everything to databases."""
        print(f"Processing file: {path}", flush=True)
        el_tree = build_tree_from_md(path)
        embeddings = self._generate_embeddings_from_tree(el_tree)

        # Add the embeddings to the vector database and save chunk info
        chunk_mongo_ids = []
        for emb in embeddings:
            vector = np.array([emb], dtype=np.float32)
            self.vector_db.add(vector)
            
            emb_id = self.vector_db.ntotal - 1
            
            new_chunk_data = {
                "vector_db_id": emb_id,
                "embedding": emb,
                "file_id": path
            }

            # Await the async database operation
            created_chunk = await chunk_controller.create_chunk(new_chunk_data)
            chunk_mongo_ids.append(emb_id)
            self.chunks[emb_id] = created_chunk

        # Store the file info in MongoDB
        new_file_data = {
            "_id": path,
            "chunks_ids": chunk_mongo_ids
        }
        # Await the async database operation
        created_file = await file_controller.create_file(new_file_data)
        self.files[path] = created_file
        print(f"Finished processing {path}. Added {len(embeddings)} chunks.", flush=True)

    def _get_chunks(self, text: str) -> list[str]:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        return text_splitter.split_text(text)

    def _get_embeddings(self, text: str) -> list[list[float]]:
        """Sends text to Gemini to get embeddings."""
        if not text.strip():
            return []
            
        chunks = self._get_chunks(text)
        if not chunks:
            return []

        try:
            result = genai.embed_content(
                model="models/text-embedding-004",
                content=chunks,
                task_type="RETRIEVAL_DOCUMENT"
            )

            return result['embedding']
        except Exception as e:
            print(f"Error getting embedding for text snippet: '{text[:50]}...'. Error: {e}", flush=True)
            return []

    def _generate_embeddings_from_tree_aux(self, node: dict) -> tuple[list[list[float]], str]:
        """
        Aux function for the _generate_embeddings_from_tree so it performs recursively.
        """
        embeddings = []

        content = node["content"]
        embeddings.extend(self._get_embeddings(content))

        # Check if we reached a leaf
        if "children" not in node or not node["children"]:
            return embeddings, content
    
        # Process the children
        child_content_list = [content]
        for child in node["children"]:
            child_embeddings, child_cumulative_content = self._generate_embeddings_from_tree_aux(child)
            embeddings.extend(child_embeddings)
            child_content_list.append(child_cumulative_content)
        
        # Perform the comulative embedding generation
        cumulative_content = "\n".join(child_content_list)
        if cumulative_content != content:
            embeddings.extend(self._get_embeddings(cumulative_content))

        return embeddings, cumulative_content
        
    
    def _generate_embeddings_from_tree(self, el_tree: list) -> list[list[float]]:
        """
        Generate the embeddings for the contents of the file in  bottom up approach,
        concatenating the contents of the children elements to the parents contents.
        """
        all_embeddings = []
        for root in el_tree:
            embeddings_from_root, _ = self._generate_embeddings_from_tree_aux(root)
            all_embeddings.extend(embeddings_from_root)
            
        return all_embeddings