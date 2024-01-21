from content.services import MovieService
from content.serializers import MovieSerializer, MovieDetailSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


class MovieViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = MovieSerializer
    service_class = MovieService

    def get_queryset(self):
        service = self.service_class()
        return service.all()

    def get_serializer_class(self):
        if self.action in ("list",):
            return MovieSerializer
        else:
            return MovieDetailSerializer
