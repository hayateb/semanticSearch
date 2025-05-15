from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO
from pydantic import BaseModel
from typing import List

from services.embeding import embed_chunks, embed_query
from services.semanticSearch import semantic_search
from services.preprocesser import parse_uploaded_files


app = FastAPI()
context_histrory = []

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_origins=origins,
    allow_headers=["*"],
    
    
)
@app.post("/uploadfile/")
class Request(BaseModel):
    query: str
    
async def create_upload_file(files: list[UploadFile] = File(...)):
        docs = await parse_uploaded_files(files)
        if not docs:
            return {"message": "No valid files were parsed."}
        
        chunks, metadata = embed_chunks(docs)
        query = " ".join([doc["text"] for doc in docs])
        query_vec = embed_query(query)
        results = semantic_search(query_vec)
        return {
            "message": "Files processed",
            "chunks": len(chunks),
            "top_3_results": results
    }
   

@app.get("/uploaddone")
async def read_root():
    return {"message": "File uploaded successfully"}


class QueryRequest(BaseModel):
    query: str
    
@app.post("/query/")

async def query_file(request: QueryRequest):
      try:
            request = request.query 
            return {}
      except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}
    
@app.get('/q')
async def get_query():
    return {"message": "Query endpoint"}



# class SearchRequest(BaseModel):
#     search: str
    
# @app.post("/search/")
# async def search_file(request: SearchRequest):
#       try:
#             search = request.search
#             return {"search": search, "message": "Search processed successfully"}
#       except Exception as e:
#             return {"error": f"An error occurred: {str(e)}"}