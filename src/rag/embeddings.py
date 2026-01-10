from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()
import chromadb
from chromadb import EmbeddingFunction, Documents, Embeddings

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        try:
            client = genai.Client(os.getenv("GOOGLE_API_KEY"))
            results = client.models.embed_content(
                model="gemini-embedding-001",
                contents=input,
                config=[types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT", output_dimensionality=768)]
            )
            print(f"Embeddings model initialized: {results.embeddings}")
            print(f"Number of embeddings generated: {len(results.embeddings.values)}")
            return results.embeddings
        except Exception as e:
            print(f"Error initializing embeddings: {e}")
            return None