from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb
import requests


def search_docs(question: str) -> str:
    # Step 1 — convert question to vector

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(question).tolist()
    
    # Step 2 — search ChromaDB for similar docs
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(name="runbooks")
    results = collection.query(
        query_embeddings=[embeddings],
        n_results=2
    )



    # Step 3 — send question + relevant docs to Ollama
    relevant_doc = results['documents'][0][0]
    
    prompt = f"""You are a DevOps assistant. 
Answer the question using only the context provided below.
If the answer is not in the context, say "I don't know".

Context:
{relevant_doc}

Question: {question}

Answer:"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2", "prompt": prompt, "stream": False},
        timeout=30
    )
    
    # Step 4 — return the answer
    answer = response.json()["response"]
    return answer
    
    # Step 4 — return Ollama's answer


if __name__ == "__main__":
    question = "high memory usage, what should I check?"
    answer = search_docs(question)
    print(f"\n🤖 Answer: {answer}")