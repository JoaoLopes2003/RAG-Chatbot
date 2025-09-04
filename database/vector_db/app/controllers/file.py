from typing import List, Dict, Any
from models.file import File

async def get_file(file_id: str) -> File | None:
    """
    Retrieves a single file document from the database by its ID.

    Args:
        file_id (str): The unique ID (_id) of the file.

    Returns:
        Optional[File]: The retrieved File object or None if not found.
    """
    return await File.get(file_id)

async def get_file_by_filename(filename: str) -> File | None:
    """
    Retrieves a single file document from the database by its filename.

    Args:
        filename (str): The attribute filename of the file. Corresponds to its folder + filename

    Returns:
        Optional[File]: The retrieved File object or None if not found.
    """
    return await File.find_one(File.filename == filename)

async def get_all_files() -> List[File]:
    """
    Retrieves all file documents from the database.

    Returns:
        List[File]: A list of all File objects.
    """
    return await File.find_all().to_list()

async def create_file(file_data: Dict[str, Any]) -> File:
    """
    Creates a new file document and saves it to the database.

    Args:
        file_data (Dict[str, Any]): A dictionary with the file data.
                                    Must include '_id' and 'chunks_ids'.
                                    Example: {"_id": "path/to/file.txt", "chunks_ids": ["id1", "id2"]}

    Returns:
        File: The newly created File object.
    """
    file_obj = File(**file_data)
    await file_obj.insert()
    return file_obj

async def update_file(file_id: str, update_data: Dict[str, Any]) -> File | None:
    """
    Updates an existing file document in the database.

    Args:
        file_id (str): The ID of the file to update.
        update_data (Dict[str, Any]): A dictionary with the fields to update.

    Returns:
        Optional[File]: The updated File object or None if not found.
    """
    file = await File.get(file_id)
    if file:
        file.set(update_data)
        await file.save()
        return file
    return None

async def delete_file(file_id: str) -> File | None:
    """
    Deletes a file document from the database.

    Args:
        file_id (str): The ID of the file to delete.

    Returns:
        Optional[File]: The deleted File object or None if not found.
    """
    file = await File.get(file_id)
    if file:
        await file.delete()
        return file
    return None