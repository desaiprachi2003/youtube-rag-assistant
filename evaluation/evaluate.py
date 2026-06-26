from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from ragas.llms import LangchainLLMWrapper
from langchain_google_genai import ChatGoogleGenerativeAI
from datasets import Dataset
import os
from dotenv import load_dotenv

load_dotenv()

# Use Gemini as the evaluator LLM
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

evaluator_llm = LangchainLLMWrapper(gemini_llm)

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
            answer_relevancy,
            context_precision
        ],
        llm=evaluator_llm
    )

    return results