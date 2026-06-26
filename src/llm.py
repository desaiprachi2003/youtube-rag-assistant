import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(question,retrieved_results):
    documents = retrieved_results["documents"][0]

    context  = "\n\n".join(documents)
    prompt = f"""
    You are a helpful AI assistant answering questions about a YouTube video.

    Use ONLY the information provided in the context.

    If the answer is found across multiple context chunks,
    combine the information and provide a complete answer.

    If the answer is partially available, provide the available information.

    If the answer is not present at all, say:
    "I couldn't find that information in the video."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

   

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )
    return response.text
