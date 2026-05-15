import os 
import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer


def load_documents(docs_folder: str) -> list[dict]:
    documents = []
    folder_path = Path(docs_folder)
    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix == ".md":
            content = file_path.read_text(encoding='utf-8')
            documents.append({
                "filename": file_path.name,
                "content": content
            })
    return documents
                

def index_documents(docs_folder: str) -> None:    
    documents = load_documents(docs_folder) 

    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(name="runbooks")


    model = SentenceTransformer("all-MiniLM-L6-v2")

    for doc in documents:
        embedding = model.encode(doc["content"]).tolist()
        collection.add(
            ids=[doc["filename"]],
            embeddings=[embedding],
            documents=[doc["content"]],
            metadatas=[{"filename": doc["filename"]}]
        )
        print(f"✅ Indexed: {doc['filename']}")    

if __name__ == "__main__":
    index_documents("docs")


