from src.downloader import download_audio
from src.transcriber import transcribe_audio
from src.chunker import chunk_text
from src.embeddings import create_embeddings
from src.vectordb import store_embeddings, video_exists
from src.retriever import retrieve_chunks
from src.llm import generate_answer

def process_video(url):
    audio_file, metadata = download_audio(url)

    if video_exists(metadata["video_id"]):
        print("Video already processed!")
        return metadata["video_id"]
    transcript = transcribe_audio(audio_file)
    chunks = chunk_text(transcript)
    embeddings = create_embeddings(chunks)
    store_embeddings(chunks,embeddings,metadata)
    return metadata["video_id"]

def ask_question(question, video_id):
    retrieved_results = retrieve_chunks(question, video_id)

    answer = generate_answer(question, retrieved_results)

    return {
        "answer": answer,
        "contexts": retrieved_results["documents"][0]
    }


