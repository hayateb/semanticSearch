import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from services.embeding import embedded_chunks, chunk_metadata
def semantic_search(query_vec, chunks, metadata, top_k=3):
    
    if query_vec is None or len(query_vec) == 0:
        raise ValueError("Query vector is empty.")

    if len(query_vec.shape) == 1:
        query_vec = query_vec.reshape(1, -1)

    similarities = cosine_similarity(query_vec, chunks)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    results = []
    for i in top_indices:
        result = metadata[i].copy()
        result["score"] = float(similarities[i])
        results.append(result)
    return results
