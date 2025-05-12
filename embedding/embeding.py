from sentence_transformers import SentenceTransformer
from semanticSearch.cleaning.preprocesser import preprocess_text
import pandas as pd
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
def embed_text(text):
      if not text:
            return np.array([])
      
      preprocessed_text = preprocess_text(text)
      
      embeddings = model.encode(preprocessed_text)
      
      return embeddings

