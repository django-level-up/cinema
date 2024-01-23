from celery import shared_task, current_task
import time
from content.models import (
    Source,
    Movie,
    MovieSource,
)
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger
from content.services import get_movie_info_kp


logger = get_task_logger(__name__)


@shared_task(bind=True, soft_time_limit=3600)
def update_movies_kp(self):
    try:
        kp_source, _ = Source.objects.get_or_create(
            slug="kinopoisk", defaults={"title": "kinopoisk"}
        )
        for movie in Movie.objects.all():
            data_dict = get_movie_info_kp(query=str(movie.title))
            if data_dict:
                rating = data_dict.get("rating", {})
                url = data_dict.get("url", None)
                watch = data_dict.get("watch_link", None)
                if rating:
                    movie.kinopoisk_rating = float(rating)
                    movie.save()
                filtered, created = MovieSource.objects.get_or_create(
                    movie=movie, source=kp_source
                )
                if url:
                    filtered.kinopoisk_link = url
                    filtered.watch_link = watch

                filtered.save()
                print("Movie-" + str(movie.title) + "updated from KINOPOISK")
                time.sleep(2)

            else:
                time.sleep(1)

        countdown = 60
        current_task.apply_async(countdown=countdown)

    except SoftTimeLimitExceeded:
        logger.warning("Task time limit exceeded. Restarting the task.")
        update_movies_kp.apply_async(countdown=60)
