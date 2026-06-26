from src.vectordb import collection
from src.embeddings import model

def retrieve_chunks(query,video_id):
    query_embedding = model.encode(query)
    results = collection.query(
        query_embeddings = [query_embedding.tolist()],
        n_results = 3,
        where = {"video_id":video_id}
    )
    return results
