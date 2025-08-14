from pathlib import Path
from docx2python import docx2python
import lxml.etree as ET
from document2text_server.utils.convertDoc2docx import convert_doc_to_docx

def simple_xml_extract(doc_result):
    """Simple function to extract and print XML"""
    elements = extract_lxml_elements(doc_result.officeDocument_pars)
    
    for i, elem in enumerate(elements):
        print(f"--- Element {i+1} ---")
        xml_str = ET.tostring(elem, encoding='unicode', pretty_print=True)
        print(xml_str)

def main():

    pathlist = Path('../documents/').glob('*.doc*')
    for path in pathlist:
        
        # Checks if the file is a .doc file
        if path.suffix == '.doc':
            converted_path = convert_doc_to_docx(path)
            if converted_path and converted_path.exists():
                doc_result = docx2python(converted_path)
                # Clean up converted file
                converted_path.unlink()
        elif path.suffix == '.docx':
            doc_result = docx2python(path)
        
        print(dir(doc_result))
        # print(doc_result.body_pars)
        print(doc_result.header)
        print('--------------')
        print(doc_result.officeDocument_pars)
        print('--------------')
        print(doc_result.document)
        print('--------------')

if __name__ == "__main__":
    main()