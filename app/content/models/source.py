from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models


class Source(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Source"
