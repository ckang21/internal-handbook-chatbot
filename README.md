# 🧠 Internal Handbook Chatbot

A simple AI chatbot that answers natural language questions using a company's internal handbook or HR document. It uses vector embeddings and semantic search to find the most relevant information.

## 🔍 Features

- Parses and chunks a raw employee handbook text file
- Generates embeddings using `sentence-transformers`
- Stores embeddings in a FAISS vector index
- Accepts user questions via CLI
- Returns relevant answers from the source document

## 🛠️ Tech Stack

- Python 3.9+
- FAISS (`faiss-cpu`)
- Sentence Transformers (`all-MiniLM-L6-v2`)
- CLI (optional future upgrade: Streamlit)

## 🚀 Setup

```bash
git clone https://github.com/yourusername/internal-handbook-chatbot.git
cd internal-handbook-chatbot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# 🧠 Internal Handbook Chatbot

A simple AI chatbot that answers natural language questions using a company's internal handbook or HR document. It uses vector embeddings and semantic search to find the most relevant information.

## 🔍 Features

- Parses and chunks a raw employee handbook text file
- Generates embeddings using `sentence-transformers`
- Stores embeddings in a FAISS vector index
- Accepts user questions via CLI
- Returns relevant answers from the source document

## 🛠️ Tech Stack

- Python 3.9+
- FAISS (`faiss-cpu`)
- Sentence Transformers (`all-MiniLM-L6-v2`)
- CLI (optional future upgrade: Streamlit)

## 🚀 Setup

```bash
git clone https://github.com/yourusername/internal-handbook-chatbot.git
cd internal-handbook-chatbot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt```

## 1. Add your handbook text
- Insert desired HR/IT document in data/handbook.txt

## 2. Run the pipeline
```python scripts/split_text.py
python scripts/generate_embeddings.py
python scripts/chatbot_cli.py```

## Example
- 🧠 Internal Handbook Chatbot
- Type your question (or 'exit' to quit):

- ❓ You: What is the vacation policy?

- 💬 Bot:
- Vacation time must be requested two weeks in advance

## Future plans
- Add a Streamlit-based web UI
- Return multiple top-matching chunks with better formatting
- Integrate an LLM to rephrase and summarize answers
- Add support for multiple documents or sections