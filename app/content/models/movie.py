from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models

# from django.utils.text import slugify
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
    sources = models.ManyToManyField(
        "content.MovieSource",
        related_name="movie_sources",
    )
    
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

    def __str__(self) -> str:
        return self.title
