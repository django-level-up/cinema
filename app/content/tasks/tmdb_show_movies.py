from celery import shared_task
import time
from content.models import Movie, Source, MovieSource, Show, ShowSource
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger
from PyMovieDb import IMDB
from content.services import get_movie_info_tmdb
from django.conf import settings

token = settings.KINOPOISK_TOKEN

imdb = IMDB()
logger = get_task_logger(__name__)

@shared_task(bind=True, soft_time_limit=None)
def update_movies_tmdb(self):
    try:
        tmdb_source, _ = Source.objects.get_or_create(
            slug="tmdb", defaults={"title": "tmdb"}
        )

        while True:
            for movie in Movie.objects.all():
                data_dict = get_movie_info_tmdb(str(movie.title))
                if data_dict:
                    rating = data_dict.get("rating", None)
                    url = data_dict.get("movie_url", None)
                    if rating:
                        movie.tmdb_rating = float(rating)
                        movie.save()
                    if url:
                        filtered, _ = MovieSource.objects.get_or_create(
                            movie=movie, source=tmdb_source
                        )
                        filtered.tmdb_link = url
                        filtered.save()
                    print("Movie-" + str(movie.title) + " updated from TMDB")

                time.sleep(1)

            # countdown = 60
            # current_task.apply_async(countdown=countdown)

    except SoftTimeLimitExceeded:
        logger.warning("Task time limit exceeded. Restarting the task.")
        update_movies_tmdb.apply_async(countdown=60)

@shared_task(bind=True, soft_time_limit=None)
def update_shows_tmdb(self):
    try:
        tmdb_source, _ = Source.objects.get_or_create(
            slug="tmdb", defaults={"title": "tmdb"}
        )

        while True:
            for show in Show.objects.all():
                data_dict = get_movie_info_tmdb(str(show.title))
                if data_dict:
                    rating = data_dict.get("rating", None)
                    url = data_dict.get("movie_url", None)
                    if rating:
                        show.tmdb_rating = float(rating)
                        show.save()
                    if url:
                        filtered, created = ShowSource.objects.get_or_create(
                            show=show, source=tmdb_source
                        )
                        filtered.tmdb_link = url
                        filtered.save()
                    print("Show-" + str(show.title) + " updated from TMDB")
                time.sleep(1)

            # countdown = 60
            # current_task.apply_async(countdown=countdown)

    except SoftTimeLimitExceeded:
        logger.warning("Task time limit exceeded. Restarting the task.")
        # update_shows_tmdb.apply_async(countdown=60)
