from src.rag_pipeline import process_video, ask_question

url = input("Enter YouTube URL: ")
video_id = process_video(url)
print(f"\nVideo ID: {video_id}")
while True:
    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = ask_question(question, video_id)

    print("\nAnswer:")
    print(answer)