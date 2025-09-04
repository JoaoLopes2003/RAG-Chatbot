from services.vector_db import Vector_db
from typing import Optional

# This global variable will hold the single, shared instance of our Vector_db
vector_db_instance: Optional[Vector_db] = None

def get_vector_db() -> Vector_db:
    """
    Dependency function that FastAPI will call to get the shared Vector_db instance.
    This function's only job is to return the instance that was created on startup.
    """
    return vector_db_instance
