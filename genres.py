
#To fetche and cache movie genres from the TMDB API.
import requests

GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
API_KEY = 'e3bd1daa94b3b517d13d8f4cff921430'

# Cache for storing genre data
genre_cache = {}

def fetch_genres():
    #Fetches the list of genres from the TMDB API and caches the result.
    
    #Returns - dict: A dictionary to map genre names to their respective genre IDs

    global genre_cache
    # Return cached genres if available to avoid duplicate requests
    if genre_cache:
        return genre_cache

    try:
        # Make a request to the TMDB API
        response = requests.get(GENRE_URL, params={'api_key': API_KEY})
        response.raise_for_status()
        # Analyse the response and cache the genres to avoid duplicate/excess requests
        genres = response.json().get('genres', [])
        genre_cache = {genre['name']: genre['id'] for genre in genres}
        return genre_cache
    except requests.RequestException as e: 
        # Handle request errors/Exception Handlings
        print(f"Error fetching genres: {e}")
        return {}