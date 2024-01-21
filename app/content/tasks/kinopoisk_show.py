from celery import shared_task, current_task
import time
from content.models import (
    Source,
    Show,
    ShowSource,
    Season,
)
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger
from PyMovieDb import IMDB
from content.services import get_seasons_info_kp, get_tv_show_info_kp
from django.conf import settings


token = settings.KINOPOISK_TOKEN

imdb = IMDB()
logger = get_task_logger(__name__)


@shared_task(bind=True, soft_time_limit=3600)
def update_shows_kp(self):
    try:
        kp_source = Source.objects.filter(slug="kinopoisk").first()
        if not kp_source:
            kp_source = Source.objects.create(title="kinopoisk")

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
                time.sleep(5)

            else:
                time.sleep(1)

        countdown = 60
        current_task.apply_async(countdown=countdown)

    except SoftTimeLimitExceeded:
        logger.warning("Task time limit exceeded. Restarting the task.")
        update_shows_kp.apply_async(countdown=60)


# @shared_task(bind=True, soft_time_limit=3600)
# def update_shows_kp(self):
#     try:
#         kp_source = Source.objects.filter(slug="kinopoisk").first()
#         if not kp_source:
#             kp_source = Source.objects.create(title="kinopoisk")

#         for show in Show.objects.all():
#             data_dict = get_tw_show_info_kp(query=show.title)
#             if data_dict:
#                 rating = data_dict.get("rating", {})
#                 url = data_dict.get("url", None)
#                 movie_id = data_dict.get("id", None)
#                 if rating:
#                     show.kinopoisk_rating = float(rating)
#                 if movie_id:
#                     data_dict_season = get_seasons_info_kp(movie_id=movie_id)
#                     if data_dict_season:
#                         Season.objects.all().delete()

#                         for item in data_dict_season:
#                             title = item.get("name", None)
#                             description = item.get("description", None)

#                             Season.objects.create(
#                                 title=str(title),
#                                 description=str(description),
#                                 show=show,
#                             )
#                         print("Season-" + str(title) + f"added to {show.title}")

#                 show.save()

#                 filtered, created = ShowSource.objects.get_or_create(
#                     show=show, source=kp_source
#                 )
#                 if url:
#                     filtered.download_link = url
#                 filtered.save()
#                 print("Show-" + str(show.title) + "updated from kinopoisk")

#                 time.sleep(1)
#             else:
#                 time.sleep(1)
#                 print("Limit with this token 200 queries has been expired try tomorrow")

#         countdown = 60
#         current_task.apply_async(countdown=countdown)

#     except SoftTimeLimitExceeded:
#         logger.warning("Task time limit exceeded. Restarting the task.")
#         update_shows_kp.apply_async(countdown=60)
