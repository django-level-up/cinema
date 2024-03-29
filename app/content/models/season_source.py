from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models


class SeasonSource(BaseModel):
    show = models.ForeignKey(
        "content.Show",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

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
    valid_source = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Got {self.season.title} on {self.source.title}"

    class Meta:
        verbose_name = "6. Season Source"
        verbose_name_plural = "6. Season Sources"
        unique_together = ("source", "show", "season")
