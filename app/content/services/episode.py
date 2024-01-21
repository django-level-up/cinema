from common.services import CRUDService
from content.models import Episode


class EpisodeService(CRUDService):
    class Meta:
        model = Episode
