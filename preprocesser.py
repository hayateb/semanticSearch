from io import BytesIO
import pandas as pd
import fitz
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from fastapi import FastAPI , File , UploadFile 

app = FastAPI()
@app.post("/uploadfile/")


async def create_upload_file(file: UploadFile = File(...)):
      contents = await file.read()
      df = pd.read_csv(BytesIO(contents))
      return {"filename" : file.filename}

@app.get("/")
async def read_root():
    return {"message": "welcome to the semantic search API"}

def preprocess_file(contents , filetype):
      parser ={
              'csv': pd.read_csv,
              'json': pd.read_json,
              'xlsx': pd.read_excel,
              'txt': lambda contents: contents.decode('utf-8'),
              'pdf':extract_text_from_pdf
      }
      if filetype not in parser:
          raise ValueError("Unsupported file type")
      if filetype == 'pdf':
            return parser[filetype](contents)
      return parser[filetype](BytesIO(contents)).to_csv()
def extract_text_from_pdf(contents):
      pdf_document = fitz.open(stream=contents, filetype="pdf")
      text = ""
      for page in pdf_document:
          text += page.get_text()
      pdf_document.close()
      return text
      