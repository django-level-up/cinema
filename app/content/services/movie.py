from django.conf import settings
from common.services import CRUDService
from content.models import Movie
from tmdbv3api import Movie as Film
from tmdbv3api import TMDb
import requests
import random

tmdb = TMDb()
tmdb.api_key = settings.TMDB_API_KEY


def mixing_token():
    tokens = [
        settings.KINOPOISK_TOKEN,
        settings.KINOPOISK_TOKEN2,
        settings.KINOPOISK_TOKEN3,
        settings.KINOPOISK_TOKEN4,
    ]

    return random.choice(tokens)


class MovieService(CRUDService):
    class Meta:
        model = Movie


def get_imdb_id(url):
    if url:
        imdb_id = url.split("/")[-2] if "/" in url else None
        return imdb_id
    else:
        return None


def get_movie_info_tmdb(search_query):
    movie = Film()
    try:
        search = movie.search(search_query)
    except Exception as e:
        print(f"An error occurred during TMDB search: {e}")
        search = None

    if search and search.results:
        first_result = search.results[0]
        movie_url = f"https://www.themoviedb.org/movie/{first_result.id}"

        return {
            "title": first_result.title,
            "rating": first_result.vote_average,
            "movie_url": movie_url,
        }
    else:
        return None


def get_movie_info_kp(query):
    url = "https://api.kinopoisk.dev/v1.4/movie/search"
    params = {
        "page": 1,
        "limit": 1,
        "query": query,
    }
    headers = {
        "accept": "application/json",
        "X-API-KEY": f"{mixing_token()}",
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("docs"):
            movie_data = data["docs"][0]
            movie_info = {
                "id": movie_data["id"],
                "rating": movie_data["rating"]["kp"],
                "url": f'https://www.kinopoisk.ru/film/{movie_data["id"]}',
                "watch_link": f'https://www.kinopoisk.gg/film/{movie_data["id"]}',
            }
            return movie_info
        else:
            pass
    else:
        print(f"Kinopoisk API returned limit expired {response.status_code}")

    return None
