from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models
from .episode_source import EpisodeSource


class Episode(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    season = models.ForeignKey(
        "content.Season",
        on_delete=models.CASCADE,
        related_name="episodes",
    )

    duration = models.CharField(  # Стандарт ISO 8601
        max_length=255,
        null=True,
        blank=True,
    )

    episode_sources = models.ManyToManyField(
        "content.Source",
        through="content.EpisodeSource",
        related_name="episode",
    )

    def add_source(
        self,
        source,
        download_link,
        kinopoisk_link,
        imdb_link,
    ):
        if source not in self.episode_sources.all():
            EpisodeSource.objects.create(episode=self, source=source)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "7. Episode"
        verbose_name_plural = "7. Episode"
