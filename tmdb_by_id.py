import requests
from config import Config
session = requests.Session()
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


def get_movie_details(tmdb_id):
    """
    Fetch movie details using TMDB ID.
    """

    if not tmdb_id:
        return None

    url = f"{BASE_URL}/movie/{int(tmdb_id)}"

    params = {
        "api_key": Config.TMDB_API_KEY
    }

    try:
        response = session.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        movie = response.json()

        poster = (
            IMAGE_BASE_URL + movie["poster_path"]
            if movie.get("poster_path")
            else ""
        )

        return {
            "poster": poster,
            "overview": movie.get("overview", ""),
            "release_date": movie.get("release_date", ""),
            "tmdb_rating": movie.get("vote_average", 0),
            "tmdb_id": movie.get("id")
        }

    except Exception as e:
        print("TMDB Error:", e)
        return {
            "poster": "",
            "overview": "",
            "release_date": "",
            "tmdb_rating": "N/A",
            "tmdb_id": tmdb_id
        }