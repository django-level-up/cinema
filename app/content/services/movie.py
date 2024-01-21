from django.conf import settings
from common.services import CRUDService
from content.models import Movie

token = settings.KINOPOISK_TOKEN


class MovieService(CRUDService):
    class Meta:
        model = Movie


def get_imdb_id(url):
    if url:
        imdb_id = url.split("/")[-2] if "/" in url else None
        return imdb_id
    else:
        return None
