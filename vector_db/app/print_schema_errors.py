import json
from pathlib import Path

def write_validation_errors_to_file(errors_path: str, file_path: Path, validation_errors: dict):
    """Write detailed validation errors to a file"""
    
    # Create errors directory if it doesn't exist
    errors_dir = Path(errors_path)
    try:
        errors_dir.mkdir(parents=True, exist_ok=True)  # Added parents=True
    except Exception as e:
        print(f"❌ Could not create errors directory '{errors_path}': {e}")
        return
    
    # Create error file with same name as original JSON file
    error_file_path = errors_dir / f"{file_path.stem}_errors.txt"
    
    with open(error_file_path, 'w', encoding='utf-8') as error_file:
        error_file.write(f"Validation errors for file: {file_path.name}\n")
        error_file.write("=" * 60 + "\n\n")
        
        for schema_name, error in validation_errors.items():
            error_file.write(f"Schema: {schema_name}\n")
            error_file.write("-" * 30 + "\n")
            
            for i, err in enumerate(error.errors(), 1):
                location = " -> ".join(str(loc) for loc in err['loc']) if err['loc'] else "root"
                error_type = err['type']
                message = err['msg']
                
                error_file.write(f"{i}. Location: {location}\n")
                error_file.write(f"   Error Type: {error_type}\n")
                error_file.write(f"   Message: {message}\n")
                
                # Show the actual input value that caused the error
                if 'input' in err and err['input'] is not None:
                    input_val = err['input']
                    if isinstance(input_val, (dict, list)):
                        # Truncate large objects for readability
                        input_str = str(input_val)
                        if len(input_str) > 200:
                            input_str = input_str[:197] + "..."
                        error_file.write(f"   Input: {input_str}\n")
                    else:
                        error_file.write(f"   Input: {input_val}\n")
                
                # Show context for the error if available
                if 'ctx' in err and err['ctx']:
                    ctx = err['ctx']
                    if 'expected' in ctx:
                        error_file.write(f"   Expected: {ctx['expected']}\n")
                    if 'given' in ctx:
                        error_file.write(f"   Given: {ctx['given']}\n")
                
                error_file.write("\n")  # Empty line between errors
            
            error_file.write("\n")  # Empty line between schemas
        
        # Add JSON content preview for reference
        error_file.write("JSON Content Preview:\n")
        error_file.write("-" * 30 + "\n")
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                json_content = json.load(json_file)
                json_str = json.dumps(json_content, indent=2, ensure_ascii=False)
                if len(json_str) > 1000:
                    json_str = json_str[:997] + "..."
                error_file.write(json_str)
        except Exception as e:
            error_file.write(f"Could not read JSON content: {e}")