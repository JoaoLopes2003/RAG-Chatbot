import google.generativeai as genai
import faiss
import numpy as np
import xml.etree.ElementTree as ET
import copy

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

                # Add the info about the number of rows and columns
                self.documents_bd[id]["n_rows"] = component["n_rows"]
                self.documents_bd[id]["n_columns"] = component["n_columns"]
            
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
    
    def __get_child_ids(self, id):

        child_ids = []

        # Check if the doc has children
        doc = self.documents_bd[id]
        children = doc.get("children", [])

        # Add the immediate childs if they exist
        if children:
            child_ids.extend(children)

            # Add the children of the children if they have
            for child_id in children:
                child_ids.extend(self.__get_child_ids(child_id))
        
        return child_ids
    
    def __filter_query_results(self, docs):

        relevant_docs = []
        
        # Filter the documents below a certain threshold
        threshold = 0.8
        for doc in docs:
            d, _, _ = doc
            if d < threshold:
                relevant_docs.append(doc)
        
        # Filter the documents that are children of other relevant documents
        is_child_list = [False] * len(relevant_docs)
        relevant_docs_ids = [id for _, _, id in relevant_docs]
        for index, i in enumerate(relevant_docs_ids):

            # Skip to the next if it's a child of another doc
            if is_child_list[index]:
                continue

            # Flag the children from the relevant documents list
            child_ids = self.__get_child_ids(i)
            is_child_list =  [id in child_ids for id in relevant_docs_ids]

        # Remove the children that were found
        relevant_docs = [doc for is_child, doc in zip(is_child_list, relevant_docs) if not is_child]

        return relevant_docs

    def __get_parent_id(self, id):

        # Retrieves the parent id in case it has a parent, otherwise retrieves its own id
        parent_id = self.documents_bd[id]["parent"]

        return parent_id if parent_id else id

    def __build_doc_tree(self, id):

        # Add the self node
        el = self.documents_bd[id]
        tree = copy.deepcopy(el)

        # Add self id
        tree["id"] = id

        # Check if the element has more children
        if not (el["type"] == "table"):
            children = el.get("children", [])
            if children:
                tree["children"] = [self.__build_doc_tree(child_id) for child_id in children]
            
        else:
            head_children = el.get("head_children", [])
            body_children = el.get("body_children", [])
            if head_children:
                tree["head_children"] = [self.__build_doc_tree(child_id) for child_id in head_children]
            if body_children:
                tree["body_children"] = [self.__build_doc_tree(child_id) for child_id in body_children]
        
        return tree
    
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
            docs.append((d.item(), doc, i))
        
        # Filter irrelevant docs and documents that are children of others
        relevant_docs = self.__filter_query_results(docs)

        # Return to the parent level of each document for bigger context
        relevant_docs = set([id for _, _, id in relevant_docs])
        relevant_docs = [self.__get_parent_id(id) for id in relevant_docs]

        # Remove duplicate parents
        relevant_docs = set(relevant_docs)

        # Build the document tree by adding its children
        relevant_docs_trees = []
        for id in relevant_docs:
            relevant_docs_trees.append(self.__build_doc_tree(id))
        
        return relevant_docs_trees

    def __get_elem_xml(self, element):

        # Check if the element is a text element
        if element["type"] == "text":
            elem = ET.Element('text', id=str(element["id"]), text_value=element["value"], parent_id=str(element["parent"]))

            # Check if the element has children
            children = element.get("children", [])
            if children:

                # Create a subscetions element
                subsections = ET.SubElement(elem, 'subsections')
                for child in children:
                    subsection = ET.SubElement(subsections, 'subsection')
                    subsection.append(self.__get_elem_xml(child))
        
        # Check if the element is a table element
        elif element["type"] == "table":

            # Get the number of rows and columns
            n_columns = element["n_columns"]

            elem = ET.Element('table', id=str(element["id"]), n_columns=str(n_columns), parent_id=str(element["parent"]))

            # Create the table row element for the header
            tr = ET.SubElement(elem, 'tr')

            n_columns_inserted = 0
            for header_el in element["head_children"]:
                th = ET.SubElement(tr, 'th')
                th.text = header_el["value"]
                n_columns_inserted +=1
            
            # If there are columns missing, insert empty ones
            for i in range(n_columns_inserted, n_columns):
                th = ET.SubElement(tr, 'th')

            # Insert the rows of the body of the table
            n_columns_inserted = 0
            n_rows_inserted = 1
            for body_el in element["body_children"]:
                if n_columns_inserted % n_columns == 0:
                    tr = ET.SubElement(elem, 'tr')
                    n_rows_inserted += 1
                    n_columns_inserted = 0

                td = ET.SubElement(tr, 'td')
                td.text = body_el["value"]
                n_columns_inserted += 1

            # If there are columns missing, insert empty ones
            for i in range(n_columns_inserted, n_columns):
                td = ET.SubElement(tr, 'td')

            # Add an attribute to the table element referring the number of rows
            elem.attrib["n_rows"] = str(n_rows_inserted)
        
        return elem

    
    def doc_to_xml(self, doc, doc_id):

        # Convert the doc to xml format
        root = ET.Element('document', doc_number=str(doc_id))
        sections = ET.SubElement(root, 'sections')

        # Check if the document has multiple sections
        if doc["type"] == "document":

            # Create a section for each children
            for el in doc["children"]:
                sec = ET.SubElement(sections, 'section')
                section_content = self.__get_elem_xml(el)
                section_content.attrib.pop('parent_id', None)
                sec.append(section_content)

        else:
            sec = ET.SubElement(sections, 'section')
            section_content = self.__get_elem_xml(doc)
            section_content.attrib.pop('parent_id', None)
            sec.append(section_content)
        
        return root

    def db_to_string(self):
        return self.documents_bd
