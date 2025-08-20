from fastapi import APIRouter, Response
from services.search_engine import get_relevant_docs
from schemas.server.search import QueryRequest, QueryResponse

import xml.etree.ElementTree as ET
from xml.dom import minidom

router = APIRouter()

@router.post("/", response_model=QueryResponse)
def query_search_engine(query_req: QueryRequest):
    docs_xml = get_relevant_docs(query_req.query)

    # Wrap in <results> so it’s valid XML
    xml_response = "<results>" + "".join(docs_xml) + "</results>"

    for doc in docs_xml:
        pretty_xml = minidom.parseString(doc).toprettyxml(indent="  ")
        print(pretty_xml)

    print(xml_response)
    return QueryResponse(response=xml_response, media_type="application/xml")