from pymilvus import model
from dotenv import load_dotenv
import os

load_dotenv()

gemini_ef = model.dense.GeminiEmbeddingFunction(
    model_name="models/text-embedding-004",
    api_key=os.getenv("GOOGLE_API_KEY")
)

def embed_docs(docs):
    """Generate embeddings for a list of documents using Gemini Embedding Function."""
    try:
        doc_embeddings = gemini_ef.encode_documents(docs)
        
    except Exception as e:
        print("Error embedding documents: {e}")