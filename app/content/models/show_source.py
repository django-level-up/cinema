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

    kinopoisk_link = models.URLField(
        null=True,
        blank=True,
    )
    imdb_link = models.URLField(
        null=True,
        blank=True,
    )

    download_link = models.URLField(
        null=True,
        blank=True,
    )
    
    valid_source = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Show Source"
        verbose_name_plural = "Shows Sources"
        unique_together = ("source", "show")