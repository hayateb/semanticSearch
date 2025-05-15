from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from services.embeding import embed_chunks, embed_query
from services.semanticSearch import semantic_search
from services.preprocesser import parse_uploaded_files

app = FastAPI()
context_history = []

# In-memory store for uploaded content
stored_chunks = []
stored_metadata = []

# CORS setup
origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=origins,
    allow_headers=["*"],
)

# UploadFile endpoint
@app.post("/uploadfile/")
async def create_upload_file(files: List[UploadFile] = File(...)):
    global stored_chunks, stored_metadata
    docs = await parse_uploaded_files(files)
    if not docs:
        return {"message": "No valid files were parsed."}
    
    chunks, metadata = embed_chunks(docs)
    stored_chunks = chunks
    stored_metadata = metadata
    
    return {"metadata":metadata}
# Query endpoint
class QueryRequest(BaseModel):
    query: str

@app.post("/query/")
async def query_file(request: QueryRequest):
    global stored_chunks, stored_metadata
    try:
        query_vec = embed_query(request.query)
        results = semantic_search(query_vec, stored_chunks, stored_metadata)
        return results          


    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
