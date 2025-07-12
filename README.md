# 🧠 URL RAG Agent

A **Retrieval-Augmented Generation (RAG)** assistant that answers questions from any public **web URL**. It combines **semantic search** (via FAISS + SentenceTransformers) with **local LLM generation** (via Mistral-7B-Instruct), running entirely **offline**.

---

## 🔧 Features

* 🌐 Scrapes full article text from any URL (news, blogs, Wikipedia, etc.)
* ✂️ Chunks and embeds using [SentenceTransformers](https://www.sbert.net/)
* 🔍 Retrieves top-k chunks with FAISS
* 🧠 Answers questions using [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
* ⚡️ 100% local: no API keys or external calls required
* ✅ Dual mode: CLI for batch processing & Streamlit UI for interactive use

---

## 🚀 Quickstart

### ◾️ 1. Clone the repo

```bash
git clone https://github.com/Amoulas55/url-rag-agent.git
cd url-rag-agent
```

### ◾️ 2. Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Requires a GPU with \~24GB+ VRAM to run Mistral-7B smoothly.

---

## 💻 Run in CLI Mode

1. Add questions to `questions.txt`
2. Run:

```bash
python main.py
```

3. Answers will be saved to `results.txt`

---

## 🌐 Run in Streamlit UI

```bash
streamlit run app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Example Questions (`questions.txt`)

```
What kind of company is Nvidia and what is it best known for?
How did Nvidia influence the gaming industry?
What major acquisitions has Nvidia made?
How does Nvidia contribute to AI and machine learning?
What controversies or legal issues has Nvidia faced?
```

---

## 🧠 Powered By

* [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
* [SentenceTransformers](https://www.sbert.net/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [trafilatura](https://github.com/adbar/trafilatura)

---

## 📆 License

**MIT License**
Free to use, modify, and share. Attribution appreciated!

---

## 📩 Author

**Angelos Moulas**
GitHub: [github.com/Amoulas55](https://github.com/Amoulas55)
