from django.db import models


class TimeStampModel(models.Model):

    """Abstract model for time management"""

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta:
        abstract = True
