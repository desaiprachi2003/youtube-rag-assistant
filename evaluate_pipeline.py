from src.rag_pipeline import ask_question, process_video
from src.evaluator import evaluate_rag

# Step 1 - Video already processed, use ID directly
video_id = "dQw4w9WgXcQ"

# Step 2 - Define test questions (only 2 to save quota)
questions = [
    "What is the main topic of this video?",
    "What are the lyrics about?"
]

# Step 3 - Get answers and contexts from your RAG
answers = []
contexts = []

print("Getting answers from RAG...")
for q in questions:
    result = ask_question(q, video_id)
    answers.append(result["answer"])
    contexts.append(result["contexts"])
    print(f"Q: {q}")
    print(f"A: {result['answer'][:100]}...")
    print()

# Step 4 - Run RAGAS evaluation
print("\nRunning RAGAS evaluation...")
results = evaluate_rag(questions, answers, contexts)

# Step 5 - Print results
print("\n=== RAGAS Scores ===")
df = results.to_pandas()
print(df[["user_input", "faithfulness", "answer_relevancy"]])

print("\n=== Average Scores ===")
print(f"Faithfulness:      {df['faithfulness'].mean():.2f}")
print(f"Answer Relevancy:  {df['answer_relevancy'].mean():.2f}")

print("\n=== What the scores mean ===")
print("0.0 - 0.4 → Poor")
print("0.4 - 0.7 → Average")
print("0.7 - 1.0 → Good")