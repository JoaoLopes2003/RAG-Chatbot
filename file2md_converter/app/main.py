from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import query_translator

app = FastAPI(title="Converter from any format to markdown format API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(query_translator.router, prefix="/query_translator")