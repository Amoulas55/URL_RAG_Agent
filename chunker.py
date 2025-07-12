# chunker.py

from typing import List
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Splits the input text into overlapping chunks of approximately `chunk_size` tokens.
    Returns a list of chunk strings.
    """
    # Set up a clean Punkt tokenizer
    punkt_param = PunktParameters()
    tokenizer = PunktSentenceTokenizer(punkt_param)

    sentences = tokenizer.tokenize(text)
    chunks = []
    chunk = []

    total_tokens = 0
    for sentence in sentences:
        token_count = len(sentence.split())

        if total_tokens + token_count > chunk_size:
            chunks.append(" ".join(chunk))
            chunk = chunk[-overlap:]  # overlap from end of last chunk
            total_tokens = sum(len(s.split()) for s in chunk)

        chunk.append(sentence)
        total_tokens += token_count

    if chunk:
        chunks.append(" ".join(chunk))

    return chunks
