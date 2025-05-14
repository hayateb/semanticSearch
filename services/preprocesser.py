from io import BytesIO
import string
import pandas as pd
import fitz
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer as Lemmatizer

from fastapi import FastAPI , File , UploadFile 


nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')




def extract_file(contents , filetype):
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
def preprocess_text(text):
      if not text:
            return "" 
  
      text = text.lower()
      clean_text = text.translate(str.maketrans ('','', string.punctuation))
      
      token = word_tokenize(clean_text)
      stop_words = set(stopwords.words('english'))
      tokens = [word for word in token if word not in stop_words]
      lemmatizer = nltk.stem.WordNetLemmatizer()
      lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
      
      return ' '.join(lemmatized_tokens)

