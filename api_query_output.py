import requests
import os
import json

def query_api():
    api_url = os.getenv("API_URL")
    try:
        response = requests.get(api_url, timeout=1)
        response.raise_for_status()
        data = response.json()
        print(f"::set-output name=api_title::{data.get('title', 'NO_TITLE')}")
        print(f"::set-output name=api_response_json::{json.dumps(data)}")
        return True
    except requests.exceptions.Timeout:
        print(f"Error querying API: Request timed out after 10 seconds for URL: {api_url}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error querying API: {e} for URL: {api_url}")
        return False

if __name__ == "__main__":
    if not query_api():
        exit(1)