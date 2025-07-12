# 🧠 URL RAG Agent

A **Retrieval-Augmented Generation (RAG)** assistant that answers user questions using public URLs as context. It combines **FAISS-based semantic retrieval** with **Mistral-7B-Instruct** for high-quality, fully local answer generation.

---

## 🔧 Features

* 🌐 Reads full web articles via URL (e.g. Wikipedia, news, blogs)
* ✂️ Chunks and embeds with [SentenceTransformers](https://www.sbert.net/)
* 🔍 Retrieves top-k relevant segments using FAISS
* 🧠 Answers questions using [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
* ⚡️ Runs fully **offline**, no OpenAI API needed
* ✅ Works in **CLI batch mode** with input/output files

---

## 🚀 Quickstart

### 🔹 1. Clone the repo

```bash
git clone https://github.com/Amoulas55/url-rag-agent.git
cd url-rag-agent
```

### 🔹 2. Install dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ Requires a GPU with \~24GB+ VRAM to run Mistral efficiently.

### 🔹 3. Run in CLI Mode (Batch)

1. Add your questions to `questions.txt`
2. Run the script:

```bash
python main.py
```

3. Results will be saved in `results.txt`

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

* **Mistral-7B-Instruct** (local transformer)
* **SentenceTransformers** (embedding model)
* **FAISS** (semantic similarity search)
* **trafilatura** (web article extraction)

---

## 🪪 License

**MIT License** — Free to use, modify, and distribute. Attribution appreciated.

---

## 📬 Author

**Angelos Moulas** — [github.com/Amoulas55](https://github.com/Amoulas55)
