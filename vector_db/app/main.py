from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import search

app = FastAPI(title="Local Search API")

# Add CORS middleware (if you want to call it from a frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(search.router, prefix="/search")