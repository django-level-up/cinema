from django.apps import AppConfig
import time

class ContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'content'
    def ready(self):
            from content.tasks import update_movies, update_shows, update_shows_kp

            from django.db.models.signals import post_migrate
            from django.apps import apps

            def on_startup(**kwargs):
                update_movies.delay()
                update_shows.delay()
                update_shows_kp.delay()

            post_migrate.connect(on_startup, sender=apps.get_app_config('content'))