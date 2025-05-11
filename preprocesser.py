import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from fastapi import FastAPI , File , UploadFile 

app = FastAPI()
@app.post("/uploadfile/")

# async def create_upload_file(file: UploadFile = File(...)):
#       contents = await file.read()
      

