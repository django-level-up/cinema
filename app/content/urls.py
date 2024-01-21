from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet,
    ShowViewSet,
    SeasonViewSet,
    EpisodeViewSet,
)

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"shows", ShowViewSet, basename="show")
router.register(r"seasons", SeasonViewSet, basename="season")
router.register(r"episodes", EpisodeViewSet, basename="episode")

# print(router.urls)
app_name = "content"

urlpatterns = [
    path("", include(router.urls)),
]
