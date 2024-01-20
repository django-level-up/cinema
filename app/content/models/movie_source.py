from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models


class MovieSource(BaseModel):
    movie = models.ForeignKey(
        "content.Movie",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    source = models.ForeignKey(
        "content.Source",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    download_link = models.URLField(
        null=True,
        blank=True,
    )

    playlist_link = models.URLField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Source movie"
        verbose_name_plural = "Sources Movies"
        unique_together = ("source", "movie")
