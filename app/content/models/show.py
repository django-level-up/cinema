from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models

from django.core.validators import MinValueValidator
from .show_source import ShowSource


class Show(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

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
    
    tmdb_rating = models.FloatField(
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

    show_sources = models.ManyToManyField(
        "content.Source",
        through="content.ShowSource",
        related_name="shows",
    )

    def add_source(
        self,
        source,
        download_link,
        kinopoisk_link,
        imdb_link,
    ):
        if source not in self.show_sources.all():
            ShowSource.objects.create(show=self, source=source)

    # seems like unecuciary

    # trending_weight = models.IntegerField(
    #     null=True,
    #     blank=True,
    # )
    # subscribed_user_only = models.BooleanField(default=True)
    # web_free = models.BooleanField(default=False)
    # web_paid = models.BooleanField(default=False)
    # weight = models.IntegerField(default=5)
    # trending_weight = models.IntegerField(default=11)
    # runtime = models.IntegerField(
    #     null=True,
    #     blank=True,
    # )
    # weight = models.IntegerField(
    #     null=True,
    #     blank=True,
    # )
    #    popularity = models.IntegerField(
    #         null=True,
    #         blank=True,
    #     )

    #     is_free = models.BooleanField(default=False)
    #     is_trending = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
