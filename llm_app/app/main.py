from fastapi import FastAPI
from routes import llm

app = FastAPI(title="Local LLM API")

app.include_router(llm.router, prefix="/llm")