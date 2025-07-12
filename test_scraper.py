from url_reader import extract_article_text
from chunker import chunk_text
from embedder import Embedder

# Step 1: Read article
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
text = extract_article_text(url)

# Step 2: Chunk it
chunks = chunk_text(text, chunk_size=100, overlap=20)
print(f"✅ Total Chunks: {len(chunks)}")

# Step 3: Embed and index
embedder = Embedder()
embeddings = embedder.encode_chunks(chunks)
embedder.build_index(embeddings)
embedder.save_index()

print("✅ Embeddings created and FAISS index saved to ./faiss_index/")
