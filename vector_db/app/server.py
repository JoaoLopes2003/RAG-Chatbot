import xml.etree.ElementTree as ET
from xml.dom import minidom

from vector_db import Vector_db

def receive_queries(search_engine: Vector_db):

    while True:
            print("Enter your query:")
            query = input()

            # Check if the query is empty
            if not query.strip():
                continue

            # Get the relevant docs for this query
            docs = search_engine.query_db(query)

            # Build the xml file for each doc
            docs_xml = []
            doc_counter = 0
            for doc in docs:
                docs_xml.append(search_engine.doc_to_xml(doc, doc_counter))
                doc_counter += 1
            
            for doc in docs_xml:
                xml_str = ET.tostring(doc, encoding='unicode')
                pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="  ")
                print(pretty_xml)