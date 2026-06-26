import chromadb
import uuid
from src.config import VECTORSTORE_DIR

client = chromadb.PersistentClient(path=str(VECTORSTORE_DIR))

collection = client.get_or_create_collection(name="youtube_rag")

def store_embeddings(chunks,embeddings,metadata):
    ids = [str(uuid.uuid4()) for _ in chunks]
    collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist(),
    metadatas=[
    {
        "video_id": metadata["video_id"],
        "title": metadata["title"],
        "channel": metadata["channel"],
        "url": metadata["url"],
        "duration": metadata["duration"],
        "language": metadata.get("language","unknown"),
        "chunk_index": i
    }
    for i in range(len(chunks))
    ]
    )

def video_exists(video_id):
    results = collection.get(where={"video_id":video_id})
    return len(results["ids"]) > 0

