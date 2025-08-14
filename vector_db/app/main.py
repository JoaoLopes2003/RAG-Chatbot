import os
from pathlib import Path
import json
# import faiss
# from dotenv import load_dotenv
from pydantic import ValidationError
# import google.generativeai as genai
from schemas.validation import write_validation_errors_to_file, validate_json_data

# Import all the schema modules
from schemas.fise_produse_agropan.text import Text
from schemas.fise_produse_agropan.table import Table
from schemas.fise_produse_agropan.image import Image
from schemas.fise_produse_agropan.fise_produse_agropan import Fpa_schema

Text.model_rebuild()
Table.model_rebuild()
Fpa_schema.model_rebuild()


DOCUMENTS_PATH = '../documents_json/'
ERRORS_PATH = '../tmp/errors/'

SCHEMA_MAP = {
    "Fpa": Fpa_schema,
}

def json2list(data: dict, list: list = []) -> list:

    for el in data['content']:
        continue

def main():
    # Load the documents into the vector db
    pathlist = Path(DOCUMENTS_PATH).glob('*.json')
    total_files = 0
    matched_files = 0
    error_files = 0
    
    for path in pathlist:
        total_files += 1
        print(f"Processing: {path.name}")
        
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse JSON in {path.name}: {e}")
            continue
        except Exception as e:
            print(f"❌ Failed to read file {path.name}: {e}")
            continue

        # Validate the JSON data
        is_valid, schema_name, validation_errors = validate_json_data(SCHEMA_MAP, data)
        
        if is_valid:
            print(f"✅ {path.name} matches schema: {schema_name}")
            matched_files += 1
        else:
            print(f"❌ {path.name} doesn't match schema: {schema_name}")
            print(f"   Writing errors to: errors/{path.stem}_errors.txt")
            
            # Write errors to file
            write_validation_errors_to_file(ERRORS_PATH, path, validation_errors)
            error_files += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"📊 Processing Summary:")
    print(f"   Total files processed: {total_files}")
    print(f"   Files matching schemas: {matched_files}")
    print(f"   Files with errors: {error_files}")
    
    if error_files > 0:
        print(f"\n⚠️  Error details written to '{ERRORS_PATH}' folder")
        print(f"   Each error file is named: [original_filename]_errors.txt")

if __name__ == "__main__":
    main()













# load_dotenv()

# API_KEY = os.getenv("API_KEY")

# # Configure the API key
# genai.configure(api_key=API_KEY)

# # Generate embeddings (not a model instance)
# response = genai.embed_content(
#     model="models/text-embedding-004",
#     content="What is the meaning of life?"
# )

# # Print the embeddings
# print(response['embedding'])