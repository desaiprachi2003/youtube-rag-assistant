from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)


def chunk_text(transcript):
    chunks = text_splitter.split_text(transcript)

    return chunks

