from sentence_transformers import SentenceTransformer
from services.preprocesser import chunk_documents, clean_text
import pandas as pd
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
embedded_chunks = []
chunk_metadata = []

def embed_chunks(documents):
    chunks = chunk_documents(documents)
    texts = [clean_text(c["text"]) for c in chunks]
    vectors = model.encode(texts)
    global embedded_chunks, chunk_metadata
    embedded_chunks = vectors
    chunk_metadata = chunks
    return vectors, chunks

def embed_query(query):
    cleaned = clean_text(query)
    if not cleaned:
        return np.array([])  # return empty array to catch it early
    vector = model.encode([cleaned])[0]
    return np.array(vector)



