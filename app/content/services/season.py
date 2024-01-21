from common.services import CRUDService
from content.models import Season


class SeasonService(CRUDService):
    class Meta:
        model = Season
