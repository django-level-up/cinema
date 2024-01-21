from content.services import ShowService
from content.serializers import ShowDetailSerializer, ShowSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


class ShowViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = ShowSerializer
    service_class = ShowService

    def get_queryset(self):
        service = self.service_class()
        return service.all()

    def get_serializer_class(self):
        if self.action in ("list",):
            return ShowSerializer
        else:
            return ShowDetailSerializer
