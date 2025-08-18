import os
from pathlib import Path
import json

from dotenv import load_dotenv
from pydantic import ValidationError

from schemas.validation import write_validation_errors_to_file, validate_json_data
from vector_db import Vector_db

# Import all the schema modules
from schemas.building_blocks.text import Text
from schemas.building_blocks.table import Table
from schemas.building_blocks.image import Image
from schemas.file_schemas.file import File_schema

Text.model_rebuild()
Table.model_rebuild()
File_schema.model_rebuild()


DOCUMENTS_PATH = '../documents_json/'
ERRORS_PATH = '../tmp/errors/'
EMBEDDINGS_DIM = 768

SCHEMA_MAP = {
    "General_file": File_schema,
}

def main():

    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    # Load the documents into the vector db
    pathlist = Path(DOCUMENTS_PATH).glob('*.json')
    total_files = 0
    matched_files = 0
    error_files = 0
    search_engine = Vector_db(API_KEY, EMBEDDINGS_DIM)
    
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

            # Add the dile to the search engine database
            search_engine.add_file(data["content"])
        else:
            print(f"❌ {path.name} doesn't match schema: {schema_name}")
            print(f"   Writing errors to: errors/{path.stem}_errors.txt")
            
            # Write errors to file
            write_validation_errors_to_file(ERRORS_PATH, path, validation_errors)
            error_files += 1
        
        print(json.dumps(search_engine.db_to_string(), sort_keys=True, indent=4))

        while True:
            print("Enter your query:")
            query = input()
            docs = search_engine.query_db(query)
            for doc in docs:
                print(doc)
    
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