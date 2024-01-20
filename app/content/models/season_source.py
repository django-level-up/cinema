from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models


class SeasonSource(BaseModel):
    season = models.ForeignKey(
        "content.Season",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    source = models.ForeignKey(
        "content.Source",
        on_delete=models.CASCADE,
    )
    download_link = models.URLField(
        null=True,
        blank=True,
    )

    kinopoisk_link = models.URLField(
        null=True,
        blank=True,
    )
    imdb_link = models.URLField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Season Source"
        verbose_name_plural = "Season Sources"
