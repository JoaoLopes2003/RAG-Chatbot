import os
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
from vector_db import Vector_db
from load_files import load_files

load_dotenv()
API_KEY = os.getenv("API_KEY")
EMBEDDINGS_DIM = 768

search_engine = Vector_db(API_KEY, EMBEDDINGS_DIM)
load_files(search_engine)

def get_relevant_docs(query: str):
    docs = search_engine.query_db(query)

    results = []
    doc_counter = 0
    for doc in docs:
        xml_doc = search_engine.doc_to_xml(doc, doc_counter)
        xml_str = ET.tostring(xml_doc, encoding="unicode")
        results.append(xml_str)
        doc_counter += 1

    return results