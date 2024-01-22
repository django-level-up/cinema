from django.apps import AppConfig
import time

class ContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'content'
    def ready(self):
            from content.tasks import (update_movies, 
                                       update_shows,
                                       update_shows_kp,
                                       update_movies_tmdb,
                                       update_shows_tmdb,
                                       update_movies_kp,
                                       check_movie_source,
                                       check_show_source,
                                       )

            from django.db.models.signals import post_migrate
            from django.apps import apps

            def on_startup(**kwargs):
                    
                update_movies_kp.delay()
                update_shows_kp.delay()
                
                update_movies_tmdb.delay()
                update_shows_tmdb.delay()

                update_movies.delay() # imdb
                update_shows.delay()
                
                check_movie_source.delay()
                check_show_source.delay()
                


            post_migrate.connect(on_startup, sender=apps.get_app_config('content'))
