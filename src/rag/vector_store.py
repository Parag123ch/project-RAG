import chromadb
from ..rag.embeddings import GeminiEmbeddingFunction

def create_chroma_db(documents, name):
    try:
        chroma_client = chromadb.Client()
        db = chroma_client.create_collection(
            name=name,
            embedding_function=GeminiEmbeddingFunction()
        )
        for i, d in enumerate(documents):
            db.add(
                documents=d,
                ids=str(i)
            )
        print(f"ChromaDB collection '{name}' created with {len(documents)} documents.")
        return db
    except Exception as e:
        print(f"Error creating ChromaDB collection: {e}")
        return None