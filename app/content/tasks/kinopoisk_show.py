from celery import shared_task
import time
from content.models import Source, Show, ShowSource
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger
from PyMovieDb import IMDB
from content.services import get_tv_show_info_kp
from django.conf import settings

token = settings.KINOPOISK_TOKEN

imdb = IMDB()
logger = get_task_logger(__name__)

@shared_task(bind=True, soft_time_limit=None)
def update_shows_kp(self):
    try:
        kp_source, _ = Source.objects.get_or_create(
            slug="kinopoisk", defaults={"title": "kinopoisk"}
        )

        while True:
            for show in Show.objects.all():
                data_dict = get_tv_show_info_kp(query=str(show.title))
                if data_dict:
                    rating = data_dict.get("rating", {})
                    url = data_dict.get("url", None)
                    watch = data_dict.get("watch_link", None)
                    if rating:
                        show.kinopoisk_rating = float(rating)
                        show.save()
                    filtered, created = ShowSource.objects.get_or_create(
                        show=show, source=kp_source
                    )
                    if url:
                        filtered.kinopoisk_link = url
                        filtered.watch_link = watch

                    filtered.save()
                    print("Show-" + str(show.title) + " updated from KINOPOISK")
                    time.sleep(1)

                else:
                    time.sleep(1)

            # countdown = 60
            # current_task.apply_async(countdown=countdown)

    except SoftTimeLimitExceeded:
        logger.warning("Task time limit exceeded. Restarting the task.")
        # update_shows_kp.apply_async(countdown=60)
