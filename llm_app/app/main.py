from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import llm

app = FastAPI(title="Local LLM API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(llm.router, prefix="/llm")