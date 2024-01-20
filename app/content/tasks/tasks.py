from celery import shared_task, current_task
import time
from content.models import Movie, Source, MovieSource, Show, ShowSource
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger
from PyMovieDb import IMDB
import json
from datetime import datetime
from content.service import get_imdb_id
from django.conf import settings
# import requests

token = settings.KINOPOISK_TOKEN

imdb = IMDB()
logger = get_task_logger(__name__)


@shared_task(bind=True, soft_time_limit=3600)
def update_movies(self):
    try:
        imdb_source = Source.objects.filter(title="Imdb").first()
        if not imdb_source:
            imdb_source = Source.objects.create(title="Imdb")

        for movie in Movie.objects.all():
            data = imdb.get_by_name(movie.title, tv=False)
            data_dict = json.loads(data)

            description = data_dict.get("description", None)
            rating = data_dict.get("rating", {}).get("ratingValue", None)
            image = data_dict.get("poster", None)
            release_date_str = data_dict.get("datePublished", None)
            keywords = data_dict.get("keywords", None)
            duration = data_dict.get("duration", None)
            url = data_dict.get("url", None)
            imdb_id = get_imdb_id(url)

            if description:
                movie.description = str(description)
            if rating:
                movie.imdb_rating = float(rating)
            if image:
                movie.image = str(image)
            if duration:
                movie.duration = str(duration)
            if keywords:
                movie.keywords = str(keywords)
            if release_date_str:
                try:
                    release_date = datetime.strptime(
                        release_date_str, "%Y-%m-%d"
                    ).date()
                    movie.release_date = release_date
                except ValueError:
                    pass
            movie.save()

            filtered, created = MovieSource.objects.get_or_create(
                movie=movie, source=imdb_source
            )
            if imdb_id:
                download_link = "https://www.imdb.com/title/" + imdb_id + "/"
                filtered.download_link = download_link

            filtered.save()
            print("Movie-" + str(movie.title) + "updated from IMDb")

            time.sleep(1)

        countdown = 60
        current_task.apply_async(countdown=countdown)

    except SoftTimeLimitExceeded:
        logger.warning("Task time limit exceeded. Restarting the task.")
        update_movies.apply_async(countdown=60)


@shared_task(bind=True, soft_time_limit=3600)
def update_shows(self):
    try:
        imdb_source = Source.objects.filter(title="Imdb").first()
        if not imdb_source:
            imdb_source = Source.objects.create(title="Imdb")

        for show in Show.objects.all():
            data = imdb.get_by_name(show.title, tv=False)
            data_dict = json.loads(data)

            description = data_dict.get("description", None)
            rating = data_dict.get("rating", {}).get("ratingValue", None)
            image = data_dict.get("poster", None)
            release_date_str = data_dict.get("datePublished", None)
            keywords = data_dict.get("keywords", None)
            duration = data_dict.get("duration", None)
            url = data_dict.get("url", None)
            imdb_id = get_imdb_id(url)

            if description:
                show.description = str(description)
            if rating:
                show.imdb_rating = float(rating)
            if image:
                show.image = str(image)
            if duration:
                show.duration = str(duration)
            if keywords:
                show.keywords = str(keywords)
            if release_date_str:
                try:
                    release_date = datetime.strptime(
                        release_date_str, "%Y-%m-%d"
                    ).date()
                    show.release_date = release_date
                except ValueError:
                    pass
            show.save()

            filtered, created = ShowSource.objects.get_or_create(
                show=show, source=imdb_source
            )
            if imdb_id:
                download_link = "https://www.imdb.com/title/" + imdb_id + "/"
                filtered.download_link = download_link

            filtered.save()
            print("Show-" + str(show.title) + "updated from IMDb")

            time.sleep(1)

        countdown = 60
        current_task.apply_async(countdown=countdown)

    except SoftTimeLimitExceeded:
        logger.warning("Task time limit exceeded. Restarting the task.")
        update_shows.apply_async(countdown=60)
