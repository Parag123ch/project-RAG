from langchain_community.document_loaders import WebBaseLoader

def load_data(urls):
    try:
        docs = [WebBaseLoader(url).load() for url in urls]
        return docs
    except FileNotFoundError:
        print(f"File not found: {urls}")
        return None
    except Exception as e:
        print(f"Error loading document: {e}")
        return None