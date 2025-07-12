from rag_pipeline import answer_question_from_url

# ✅ Target article
url = "https://en.wikipedia.org/wiki/Nvidia"

# ✅ Load questions
with open("questions.txt", "r") as f:
    questions = [line.strip() for line in f if line.strip()]

# ✅ Write answers to file
with open("results.txt", "w") as out:
    out.write(f"Answers for: {url}\n\n")
    for i, question in enumerate(questions, 1):
        print(f"🔹 Question {i}: {question}")
        try:
            answer = answer_question_from_url(url, question)
        except Exception as e:
            answer = f"[Error]: {str(e)}"
        print(f"💡 Answer:\n{answer}\n{'-'*50}")
        out.write(f"Q{i}: {question}\nA{i}: {answer}\n\n")
