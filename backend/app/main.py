from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import backend

app = FastAPI(title="Entrypoint to the user.")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(backend.router, prefix="")