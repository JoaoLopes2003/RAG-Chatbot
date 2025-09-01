import os
from pathlib import Path

class FILE():
    def __init__(self, file_path: str, md_files_folder_path: str, uploaded: bool = False, converted: bool = False):

        p = Path(file_path)

        self.filename = p.stem
        self.file_extension = p.suffix
        self.folder = p.parent.name
        self.original_file_path = file_path
        self.converted = converted
        self.size = os.path.getsize(file_path)
        self.uploaded = uploaded
        self.gemini_obj = None

        # Path to the converted version of the file
        md_base_path = Path(md_files_folder_path)
        new_filename = f"{p.name}.md"
        self.md_file_path: str = str(md_base_path / self.folder / new_filename)
    
    def on_cloud(self, file_obj):
        self.uploaded = True
        self.gemini_obj = file_obj
    
    def off_cloud(self):
        self.uploaded = False
        self.gemini_obj = None
    
    def file_converted(self):
        self.converted = True