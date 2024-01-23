from celery import shared_task, current_task
import time
from content.models import ShowSource, MovieSource
from celery.utils.log import get_task_logger
from celery.exceptions import SoftTimeLimitExceeded
import requests

logger = get_task_logger(__name__)

def validate_watch_link(watch_link):
    try:
        response = requests.head(watch_link, allow_redirects=True, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False

@shared_task(bind=True, soft_time_limit=None)
def check_movie_source(self):
    try:
        while True:
            sources = MovieSource.objects.all()
            for source in sources:
                is_valid = validate_watch_link(source.watch_link)
                source.valid_source = is_valid
                source.save()
                print(f"Source of movie - {source.movie} checked")
                time.sleep(1)

            countdown = 60
            current_task.apply_async(countdown=countdown)

    except SoftTimeLimitExceeded:
        logger.warning("Task time limit exceeded. Restarting the task.")

@shared_task(bind=True, soft_time_limit=None)
def check_show_source(self):
    try:
        while True:
            sources = ShowSource.objects.all()
            for source in sources:
                is_valid = validate_watch_link(source.watch_link)
                source.valid_source = is_valid
                source.save()
                print(f"Source of show - {source.show} checked")
                time.sleep(1)

            # countdown = 60
            # current_task.apply_async(countdown=countdown)

    except SoftTimeLimitExceeded:
        logger.warning("Task time limit exceeded. Restarting the task.")
