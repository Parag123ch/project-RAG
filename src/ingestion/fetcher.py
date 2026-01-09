import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_data():
    base_url = "https://serpapi.com/search"
    params = {
    "engine": "google_patents",
    "q": "solar panel",
    "api_key": os.getenv("serpapi_key")
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        results = response.json()
        organic_results = results.get("organic_results", [])
        print(f"Number of results fetched: {len(organic_results)}")
        return organic_results
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None