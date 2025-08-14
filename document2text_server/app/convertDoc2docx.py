import subprocess

# Converts a .doc file to a .docx file
def convert_doc_to_docx(doc_path):
    """
    Convert .doc file to .docx using LibreOffice
    Requires LibreOffice to be installed
    """
    try:
        output_dir = doc_path.parent / "temp_converted"
        output_dir.mkdir(exist_ok=True)
        
        # Use LibreOffice to convert
        cmd = [
            "libreoffice", 
            "--headless", 
            "--convert-to", "docx",
            "--outdir", str(output_dir),
            str(doc_path)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            # Find the converted file
            converted_name = doc_path.stem + ".docx"
            converted_path = output_dir / converted_name
            return converted_path
        else:
            print(f"LibreOffice conversion failed: {result.stderr}")
            return None
            
    except subprocess.TimeoutExpired:
        print("LibreOffice conversion timed out")
        return None
    except FileNotFoundError:
        print("LibreOffice not found. Please install LibreOffice or use alternative method.")
        return None
    except Exception as e:
        print(f"Conversion error: {e}")
        return None