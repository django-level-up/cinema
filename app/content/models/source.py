from django.db import models
from django.utils.text import slugify
from common.models import BaseModel


class Source(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "0. Source"
        verbose_name_plural = "0. Sources"
