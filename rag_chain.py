import os
import faiss
import torch
import numpy as np
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline
)
from sentence_transformers import SentenceTransformer


class RAGPipeline:
    def __init__(self):
        # Embedding model
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

        # Load FAISS index
        self.index = faiss.read_index("faiss_index/index.faiss")
        with open("faiss_index/chunks.txt", "r", encoding="utf-8") as f:
            self.chunks = [line.strip() for line in f]

        # Load tokenizer and model for generation (using accelerate + float16)
        gen_model_name = "mistralai/Mistral-7B-Instruct-v0.1"
        self.tokenizer = AutoTokenizer.from_pretrained(
            gen_model_name,
            trust_remote_code=True,
            use_fast=False  # ✅ FIX: force slow tokenizer to avoid crash
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            gen_model_name,
            device_map="auto",
            torch_dtype=torch.float16,
            trust_remote_code=True
        )

        # Text generation pipeline
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer
        )

    def ask(self, question, top_k=5, max_tokens=300):
        # Embed the question
        question_embedding = self.embedder.encode([question])
        question_embedding = np.array(question_embedding).astype("float32")

        # Search in FAISS
        D, I = self.index.search(question_embedding, top_k)
        retrieved_chunks = [self.chunks[i] for i in I[0]]

        # Build prompt
        context = "\n\n".join(retrieved_chunks)
        prompt = (
            f"Answer the question based on the following article:\n\n{context}\n\n"
            f"Question: {question}\nAnswer:"
        )

        # Generate
        outputs = self.generator(prompt, max_new_tokens=max_tokens, do_sample=False)
        return outputs[0]["generated_text"].replace(prompt, "").strip()
