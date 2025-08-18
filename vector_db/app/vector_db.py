import google.generativeai as genai
import faiss
import numpy as np

from langchain.text_splitter import RecursiveCharacterTextSplitter

class Vector_db:
    def __init__(self, apiKey, embeddingDimention = 768):
        self.embedding_dim = embeddingDimention
        self.documents_bd = {}
        self.id_counter = 1
        self.vector_bd = faiss.IndexIDMap(faiss.IndexFlatL2(embeddingDimention))

        genai.configure(api_key=apiKey)
    
    def __get_embeddings(self, chunks):
        
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=chunks
        )

        return result
    
    def __add_docs(self, id, type, text, parent_id):

        component = None
        if type == "table":
            component = {
                "type": type,
                "parent": parent_id if parent_id else None
            }
        else:
            component = {
                "type": type,
                "value": text,
                "parent": parent_id if parent_id else None
            }
        
        # Add the new doc and respective embeddings to the document database
        self.documents_bd[id] = component
    
    def __add_chunk(self, type, text, parent_id = None):

        # In case the text is to big, we divide it in multiple documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 50,
            length_function = len,
        )
        docs = text_splitter.split_text(text)

        # Generate the embeddings for the chuncks
        id = self.id_counter
        embeddings_ids = np.array([id] * len(docs), dtype="int64")
        self.id_counter += 1
        
        result = self.__get_embeddings(docs)

        embeddings = np.array(result["embedding"], dtype="float32")
        
        # Add the embeddings to the vector database
        self.vector_bd.add_with_ids(embeddings, embeddings_ids)

        # Update the document database
        self.__add_docs(id, type, text, parent_id)

        return id

    def add_file(self, content, parent_id = None):

        children = None

        if isinstance(content, list):
            id = self.id_counter
            self.id_counter += 1
            children = []
            for component in content:
                id_child = self.add_file(component, id)
                children.append(id_child)
            
            # Add the table father element to the documents database
            self.__add_docs(id, "document", None, None)

            # Update the father with the info about the children
            self.documents_bd[id]["children"].extend(children)

        else:
            # Build component tree
            component = content
            component_type = component["type"]
            
            if component_type == "text":
                # Add chunck of text to the vector database
                value = component["value"]
                id = self.__add_chunk(component_type, value, parent_id)
                
                # In case the component has more child components, add them
                children = component.get("children", [])

            elif component_type == "image":
                id = None
                print("It's an image. We don't handle images yet.")

            elif component_type == "table":
                
                # Define the table id
                id = self.id_counter
                self.id_counter += 1

                # Treat the header data
                header_children = []
                for elem in component["header"]:
                    id_child = self.add_file(elem["el"], id)
                    header_children.append(id_child)
                
                # Treat the body data
                body_children = []
                for row in component["body"]:
                    for elem in row:
                        id_child = self.add_file(elem["el"], id)
                        body_children.append(id_child)
                
                # Add the table father element to the documents database
                self.__add_docs(id, "table", None, parent_id)
                
                # Update the father with the info about the children
                self.documents_bd[id]["head_children"] = header_children
                self.documents_bd[id]["body_children"] = body_children
            
            # Deal with children in case there are any
            if children and len(list(filter(None, children))):
                children = list(filter(None, children))
                children_ids = []
                for child in children:
                    id_child = self.add_file(child, id)
                    children_ids.append(id_child)
                
                # Add the child id to the respective parent list
                self.documents_bd[id]["children"] = children_ids
            
            return id
    
    def __filter_query_results(self, docs):

        # Add 
    
    def query_db(self, query):

        # Get the embedding for the query
        result = self.__get_embeddings(query)
        embedding = np.array(result["embedding"], dtype="float32").reshape(1, -1)

        # Search the vector database
        D, I = self.vector_bd.search(embedding, k=20)

        # Map the indexes to the respective blocks
        docs = []
        for d, i in zip(D[0], I[0]):

            # Get the text for the respective document
            doc = self.documents_bd[i]["value"]
            docs.append((d.item(), doc))
        
        relevant_docs = self.__filter_query_results(docs)

        return relevant_docs

    def db_to_string(self):
        return self.documents_bd
