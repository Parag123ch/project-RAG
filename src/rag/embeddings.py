from google.generativeai import genai

def get_embeddings(chunks):
    try:
        client = genai.Client()
        results = client.models.embed_content(
            model="gemini-embedding-001",
            contents=chunks
        )
        print(f"Embeddings model initialized: {results.embeddings}")
        return results.embeddings
    except Exception as e:
        print(f"Error initializing embeddings: {e}")
        return None