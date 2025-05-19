# scripts/chatbot_cli.py

import faiss
import pickle
from sentence_transformers import SentenceTransformer

def load_index_and_chunks():
    index = faiss.read_index("data/faiss_index.idx")
    with open("data/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

def get_top_chunk(query, model, index, chunks, k=1):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    return [chunks[i] for i in indices[0]]

if __name__ == "__main__":
    print("🧠 Internal Handbook Chatbot")
    print("Type your question (or 'exit' to quit):")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    index, chunks = load_index_and_chunks()

    while True:
        user_input = input("\n❓ You: ")
        if user_input.lower() in ("exit", "quit"):
            break

        top_chunks = get_top_chunk(user_input, model, index, chunks)
        print(f"\n💬 Bot:\n{top_chunks[0]}")
