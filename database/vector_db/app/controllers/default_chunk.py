from typing import List, Dict, Any
from beanie import PydanticObjectId
from models.default_chunk import DefaultChunk

async def get_chunk(chunk_id: PydanticObjectId) -> DefaultChunk | None:
    """
    Retrieves a single chunk document from the database by its ID.

    Args:
        chunk_id (PydanticObjectId): The unique ID (_id) of the chunk.

    Returns:
        Optional[Chunk]: The retrieved Chunk object or None if not found.
    """
    return await DefaultChunk.get(chunk_id)

async def get_chunk_by_vector_id(vector_id: int) -> DefaultChunk | None:
    """
    Retrieves a single chunk associated with a specific vector ID.

    Args:
        vector_id (int): The ID associated with the chunk in the vector database.

    Returns:
        Optional[Chunk]: The Chunk object associated with the vector ID, or None if not found.
    """
    return await DefaultChunk.find_one(DefaultChunk.vector_db_id == vector_id)

async def get_chunks_by_file_id(file_id: str) -> List[DefaultChunk]:
    """
    Retrieves all chunks associated with a specific file ID.

    Args:
        file_id (str): The ID of the parent file.

    Returns:
        List[Chunk]: A list of Chunk objects associated with the file.
    """
    return await DefaultChunk.find(DefaultChunk.file_id == file_id).to_list()

async def get_all_chunks() -> List[DefaultChunk]:
    """
    Retrieves all chunk documents from the database.

    Returns:
        List[Chunk]: A list of all Chunk objects.
    """
    return await DefaultChunk.find_all().to_list()

async def create_chunk(chunk_data: Dict[str, Any]) -> DefaultChunk:
    """
    Creates a new chunk document and saves it to the database.

    Args:
        chunk_data (Dict[str, Any]): A dictionary with the chunk data.
                                     Example: {"vector_db_id": 1, "embedding": [...], "file_id": "..."}

    Returns:
        Chunk: The newly created Chunk object.
    """
    chunk_obj = DefaultChunk(**chunk_data)
    await chunk_obj.insert()
    return chunk_obj

async def update_chunk(chunk_id: PydanticObjectId, update_data: Dict[str, Any]) -> DefaultChunk | None:
    """
    Updates an existing chunk document in the database.

    Args:
        chunk_id (PydanticObjectId): The ID of the chunk to update.
        update_data (Dict[str, Any]): A dictionary with the fields to update.

    Returns:
        Optional[Chunk]: The updated Chunk object or None if not found.
    """
    chunk = await DefaultChunk.get(chunk_id)
    if chunk:
        chunk.set(update_data)
        await chunk.save()
        return chunk
    return None

async def delete_chunk(chunk_id: PydanticObjectId) -> DefaultChunk | None:
    """
    Deletes a chunk document from the database.

    Args:
        chunk_id (PydanticObjectId): The ID of the chunk to delete.

    Returns:
        bool: True if the chunk was deleted, False otherwise.
    """
    chunk = await DefaultChunk.get(chunk_id)
    if chunk:
        await chunk.delete()
        return chunk
    return None
