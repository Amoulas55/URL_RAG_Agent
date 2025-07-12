# ~/url_rag_agent/rag_pipeline.py

from url_reader import extract_article_text
from chunker import chunk_text
from embedder import Embedder
from rag_chain import RAGPipeline

# Load the RAG model and embedder once
rag = RAGPipeline()

def answer_question_from_url(url: str, question: str) -> str:
    # 1. Extract article content
    article_text = extract_article_text(url)
    if not article_text:
        raise ValueError("Failed to extract content from the provided URL.")

    # 2. Chunk the article text
    chunks = chunk_text(article_text, chunk_size=100, overlap=20)

    # 3. Embed and build index
    embedder = Embedder()
    embeddings = embedder.encode_chunks(chunks)
    embedder.build_index(embeddings)

    # 4. Overwrite rag's index for this question with fresh one
    rag.index = embedder.index
    rag.chunks = embedder.text_chunks

    # 5. Ask the question
    return rag.ask(question)
