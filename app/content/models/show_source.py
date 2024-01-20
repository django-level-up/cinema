from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models


class ShowSource(BaseModel):
    show = models.ForeignKey(
        "content.Show",
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
        verbose_name = "Show Source"
        verbose_name_plural = "Shows Sources"
