import sys
import os

from langchain_docling import DoclingLoader
from langchain_docling.loader import ExportType
from docling.chunking import HybridChunker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import EMBED_MODEL_ID

def load_data(file_path):
    try:
        loader = DoclingLoader(
            file_path=file_path, 
            export_type=ExportType.DOC_CHUNKS,
            chunker=HybridChunker(EMBED_MODEL_ID)
        )
        docs = loader.load()
        return docs
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading document: {e}")
        return None