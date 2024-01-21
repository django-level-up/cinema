from content.services import EpisodeService
from content.serializers import EpisodeDetailSerializer, EpisodeSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

class EpisodeViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = EpisodeSerializer
    service_class = EpisodeService

    def get_queryset(self):
        service = self.service_class()
        return service.all()

    def get_serializer_class(self):
        if self.action in ("list",):
            return EpisodeSerializer
        else:
            return EpisodeDetailSerializer
