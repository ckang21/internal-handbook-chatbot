# scripts/split_text.py

import os
from typing import List
import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

def load_handbook(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def chunk_text(text: str, max_tokens: int = 500) -> List[str]:
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len((current_chunk + sentence).split()) > max_tokens:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
        else:
            current_chunk += " " + sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

if __name__ == "__main__":
    handbook_path = "data/handbook.txt"  # Update this if your path is different
    output_path = "data/chunks.txt"

    text = load_handbook(handbook_path)
    chunks = chunk_text(text)

    os.makedirs("data", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n---\n")

    print(f"Saved {len(chunks)} chunks to {output_path}")
