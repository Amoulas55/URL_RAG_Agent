# embedder.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

class Embedder:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.text_chunks = []

    def encode_chunks(self, chunks):
        """
        Encode text chunks into embeddings.
        """
        self.text_chunks = chunks
        embeddings = self.model.encode(chunks, show_progress_bar=True, convert_to_numpy=True)
        return embeddings

    def build_index(self, embeddings):
        """
        Build FAISS index from embeddings.
        """
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def save_index(self, path='faiss_index'):
        """
        Save index and associated text chunks.
        """
        if not os.path.exists(path):
            os.makedirs(path)
        faiss.write_index(self.index, os.path.join(path, 'index.faiss'))
        with open(os.path.join(path, 'chunks.txt'), 'w') as f:
            for chunk in self.text_chunks:
                f.write(chunk.replace("\n", " ") + "\n")

    def load_index(self, path='faiss_index'):
        """
        Load previously saved index and chunks.
        """
        self.index = faiss.read_index(os.path.join(path, 'index.faiss'))
        with open(os.path.join(path, 'chunks.txt'), 'r') as f:
            self.text_chunks = [line.strip() for line in f.readlines()]
