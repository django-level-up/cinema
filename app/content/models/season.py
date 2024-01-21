from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models
from .season_source import SeasonSource
# from django.utils.text import slugify


class Season(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    show = models.ForeignKey(
        "content.Show",
        on_delete=models.CASCADE,
    )

    duration = models.CharField(  # cтандарти ISO 8601
        max_length=255,
        null=True,
        blank=True,
    )

    season_sources = models.ManyToManyField(
        "content.Source",
        through="content.SeasonSource",
        related_name="season",
    )

    def add_source(
        self,
        source,
        download_link,
        kinopoisk_link,
        imdb_link,
    ):
        if source not in self.season_sources.all():
            SeasonSource.objects.create(season=self, source=source)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created"]
