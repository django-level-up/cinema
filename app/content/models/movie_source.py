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
        return f"Got {self.movie.title} on {self.source.title}"

    class Meta:
        verbose_name = "Movie Source"
        verbose_name_plural = "Movies Sources"
        unique_together = ("source", "movie")
