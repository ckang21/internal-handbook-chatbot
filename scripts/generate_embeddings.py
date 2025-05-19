# scripts/generate_embeddings.py

import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load the text chunks from file
def load_chunks(path="data/chunks.txt"):
    with open(path, "r", encoding="utf-8") as f:
        chunks = f.read().split("\n---\n")
    return [chunk.strip() for chunk in chunks if chunk.strip()]

if __name__ == "__main__":
    # 1. Load the AI model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # 2. Load your text chunks
    chunks = load_chunks()

    # 3. Generate embeddings
    embeddings = model.encode(chunks, show_progress_bar=True)

    # 4. Create a FAISS index and add embeddings
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # 5. Save index and chunks for future use
    faiss.write_index(index, "data/faiss_index.idx")
    with open("data/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print(f"Indexed {len(chunks)} chunks.")
