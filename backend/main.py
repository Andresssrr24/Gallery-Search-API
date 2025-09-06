from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .app.api.endpoints import search, upload, gallery

# TODO: db lifespan 

app = FastAPI(
    title="Gallery Search API",
    version="1.0.0",
    description="API for searching and managing gallery images",
    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search.router)
app.include_router(upload.router)
app.include_router(gallery.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Gallery Search API"}