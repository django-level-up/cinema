from content.services import SeasonService
from content.serializers import SeasonDetailSerializer, SeasonSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

class SeasonViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = SeasonSerializer
    service_class = SeasonService

    def get_queryset(self):
        service = self.service_class()
        return service.all()

    def get_serializer_class(self):
        if self.action in ("list",):
            return SeasonSerializer
        else:
            return SeasonDetailSerializer
