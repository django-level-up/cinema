from common.services import CRUDService
from content.models import Movie
import requests
from datetime import datetime
from django.conf import settings

token = settings.KINOPOISK_TOKEN


class LectureService(CRUDService):
    class Meta:
        model = Movie


def get_imdb_id(url):
    if url:
        imdb_id = url.split("/")[-2] if "/" in url else None
        return imdb_id
    else:
        return None


def get_tw_show_info_kp(query):
    token = settings.KINOPOISK_TOKEN
    url = "https://api.kinopoisk.dev/v1.4/movie/search"
    params = {
        "page": 1,
        "limit": 1,
        "query": query,
    }
    headers = {
        "accept": "application/json",
        "X-API-KEY": f"{token}",
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data.get("docs"):
            movie_data = data["docs"][0]
            release_year = str(movie_data.get("year", {}))
            formatted_release_year = datetime.strptime(release_year, "%Y").strftime(
                "%Y-%m-%d"
            )

            movie_info = {
                "id": movie_data["id"],
                "name": movie_data["enName"],
                "rating": movie_data["rating"]["kp"],
                "url": f'https://www.kinopoisk.ru/film/{movie_data["id"]}',
                "releaseYear": formatted_release_year,
                "poster": movie_data.get("poster", {}).get("url"),
            }
            return movie_info
    return None


def get_seasons_info_kp(movie_id):
    token = settings.KINOPOISK_TOKEN
    url = "https://api.kinopoisk.dev/v1.4/season"
    params = {
        "movieId": movie_id,
    }
    headers = {
        "accept": "application/json",
        "X-API-KEY": f"{token}",
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        seasons_info = []

        for season_data in data.get("docs", []):
            season_info = {
                "id": season_data.get("id", None),
                "name": season_data.get("name", None),
                "description": season_data.get("description", None),
            }
            seasons_info.append(season_info)

        return seasons_info

    return None
