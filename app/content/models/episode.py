from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models


class Episode(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pass
