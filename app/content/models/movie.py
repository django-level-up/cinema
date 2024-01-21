from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models
from .movie_source import MovieSource
from django.core.validators import MinValueValidator


class Movie(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    image = models.URLField(
        blank=True,
        null=True,
    )
    bg_image = models.URLField(
        blank=True,
        null=True,
    )

    release_date = models.DateField(
        null=True,
        blank=True,
    )

    imdb_rating = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0)],
    )
    tmdb_rating = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0)],
    )
    kinopoisk_rating = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0.0)],
    )
    duration = models.CharField(  # cтандарди ISO 8601
        max_length=255,
        null=True,
        blank=True,
    )
    keywords = models.TextField(
        null=True,
        blank=True,
    )
    movie_sources = models.ManyToManyField(
        "content.Source",
        through="content.MovieSource",
        related_name="movies",
    )

    def add_source(
        self,
        source,
        download_link,
        kinopoisk_link,
        imdb_link,
    ):
        if source not in self.movie_sources.all():
            MovieSource.objects.create(movie=self, source=source)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "1. Movie"
        verbose_name_plural = "1. Movies"

    # seems like unecuciary
    # popularity = models.IntegerField(
    #     null=True,
    #     blank=True,
    # )
    # is_free = models.BooleanField(
    #     default=False,
    # )
    # is_trending = models.BooleanField(
    #     default=False,
    # )

    # trending_weight = models.IntegerField(
    #     null=True,
    #     blank=True,
    # )
    # runtime = models.IntegerField(
    #     null=True,
    #     blank=True,
    # )
