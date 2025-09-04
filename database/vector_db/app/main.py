from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from models.file import File
from models.default_chunk import DefaultChunk
from models.smart_chunk import SmartChunk
from config.settings import settings
from routes import vector_db
from services.vector_db import Vector_db

vector_db_instance: Vector_db | None = None

# --- Database Initialization Logic ---
async def init_database():
    """Initializes the database connection and links the Beanie models."""
    print("Attempting to connect to the database...", flush=True)
    client = AsyncIOMotorClient(settings.mongo_connection_string)
    database = client[settings.mongo_db_name]
    await init_beanie(
        database=database,
        document_models=[File, DefaultChunk, SmartChunk]
    )
    print(f"Successfully connected to database '{settings.mongo_db_name}'.", flush=True)
    print("Beanie initialization complete. Models are ready to use.", flush=True)

# --- Lifespan Manager for Application Startup/Shutdown ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application startup and shutdown events.
    The database connection is established on startup.
    """
    print("Application startup...", flush=True)
    await init_database()

    # Create a vector_db instance
    global vector_db_instance
    vector_db_instance = await Vector_db.create()
    print("Vector DB instance created and initial files processed.")
    
    yield

    print("Application shutdown...")
    vector_db_instance = None

# --- FastAPI App Creation and Configuration ---
app = FastAPI(
    title="Document Search Engine API",
    lifespan=lifespan  # This manages startup and shutdown
)

# Add CORS middleware (allows frontend apps to call this API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Include API Routes ---
app.include_router(vector_db.router, prefix="")