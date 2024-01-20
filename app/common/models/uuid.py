from uuid import uuid4
from django.db import models


class UUIDModel(models.Model):

    """Base model with uuid pk"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        unique=True,
    )

    class Meta:
        abstract = True
