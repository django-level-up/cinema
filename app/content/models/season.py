from common.models import BaseModel  # Abstract model with uuid and time-stamps
from django.db import models
# from django.utils.text import slugify


class Season(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    show = models.ForeignKey(
        "content.Show",
        on_delete=models.CASCADE,
        related_name="seasons",
    )

    duration = models.CharField(  # cтандарти ISO 8601
        max_length=255,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "5. Season"
        verbose_name_plural = "5. Seasons"
