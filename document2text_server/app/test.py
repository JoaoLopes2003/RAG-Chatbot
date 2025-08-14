import docx
from simplify_docx import simplify
from pathlib import Path
import json

pathlist = Path('../documents/').glob('*.doc*')
for path in pathlist:

    # read in a document 
    my_doc = docx.Document(path)

    # coerce to JSON using the standard options
    my_doc_as_json = simplify(my_doc)

    print(json.dumps(my_doc_as_json, indent=4))