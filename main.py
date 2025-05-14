from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO
from pydantic import BaseModel

app = FastAPI()

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
async def create_upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # Attempt to decode with utf-8 and fallback to other encodings if needed
        df = pd.read_csv(BytesIO(contents), encoding='utf-8', errors='replace')
        return {"filename": file.filename, "message": "File processed successfully"}
    except UnicodeDecodeError:
        return {"error": "File encoding is not supported. Please upload a valid CSV file."}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
@app.get("/")
async def read_root():
    return {"message": "welcome to the file upload  API"}


class QueryRequest(BaseModel):
    query: str
    
@app.post("/query/")

async def query_file(request: QueryRequest):
      try:
            request = request.query 
            return {"query": request, "message": "Query processed successfully"}
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