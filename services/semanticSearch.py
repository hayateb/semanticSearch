import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from services.embeding import embedded_chunks, chunk_metadata

def semantic_search(query_vec, top_k=3):
    similarities = cosine_similarity([query_vec], embedded_chunks)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    results = []
    for i in top_indices:
        result = chunk_metadata[i].copy()
        result["score"] = float(similarities[i])
        results.append(result)
    return results