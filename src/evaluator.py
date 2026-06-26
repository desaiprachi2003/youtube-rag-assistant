from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from datasets import Dataset
import os
from dotenv import load_dotenv

load_dotenv()

# Gemini LLM for evaluation
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # ← was "gemini-1.5-flash"
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Google embeddings instead of OpenAI
gemini_embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

evaluator_llm = LangchainLLMWrapper(gemini_llm)
evaluator_embeddings = LangchainEmbeddingsWrapper(gemini_embeddings)

def evaluate_rag(questions, answers, contexts):
    data = {
        "user_input": questions,
        "response": answers,
        "retrieved_contexts": contexts
    }

    dataset = Dataset.from_dict(data)

    results = evaluate(
        dataset=dataset,
        metrics=[
            faithfulness,
            answer_relevancy
        ],
        llm=evaluator_llm,
        embeddings=evaluator_embeddings
    )

    return results