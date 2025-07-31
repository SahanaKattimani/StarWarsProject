import requests
import json

def get_films(url: str = 'https://swapi-node.vercel.app/api/films') -> dict:
    try:
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
          }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching films: {e}")
        raise
