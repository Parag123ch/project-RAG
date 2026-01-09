import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def normalize_data(data):
    results = []
    for item in data:
        results.append({
            "title": item.get("title"),
            "link": item.get("pdf"),
            "publication_date": item.get("publication_date")
        })
    return results