from fastapi import FastAPI, UploadFile, File
import pandas as pd
from io import BytesIO

app = FastAPI()
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


@app.post("/query/")
async def query_file(str):
      try:
      
            return {"query": str, "message": "Query processed successfully"}
      except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}
    

@app.post("search/")
async def search_file(str):
      try:

            return {"search": str, "message": "Search processed successfully"}
      except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}