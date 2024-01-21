from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet,
    # MovieListView,
    ShowViewSet,
)

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"shows", ShowViewSet, basename="show")


# print(router.urls)
app_name = "content"

urlpatterns = [
    path("", include(router.urls)),
    # path("movies/", MovieListView.as_view(), name="movie-list"),
    # other urlpatterns if needed
]
