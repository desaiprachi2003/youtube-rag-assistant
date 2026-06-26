from src.downloader import download_audio
from src.transcriber import transcribe_audio
from src.chunker import chunk_text
from src.embeddings import create_embeddings
from src.vectordb import store_embeddings, collection

url = input("Enter YouTube URL: ")

audio_file = download_audio(url)

transcript = transcribe_audio(audio_file)

chunks = chunk_text(transcript)

embeddings = create_embeddings(chunks)

store_embeddings(chunks, embeddings)

print("Embeddings stored successfully!")

print("\nTotal Documents in ChromaDB:")
print(collection.count())