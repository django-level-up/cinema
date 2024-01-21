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
    tmdb_link = models.URLField(
        null=True,
        blank=True,
    )
    valid_source = models.BooleanField(default=False)
    watch_link = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"Got {self.show.title} on {self.source.title}"

    class Meta:
        verbose_name = "4. Show Source"
        verbose_name_plural = "4. Shows Sources"
        unique_together = ("source", "show")
