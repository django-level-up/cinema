from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from common.models import BaseModel
from .user_manager import UserManager


class User(
    AbstractBaseUser,
    PermissionsMixin,
    BaseModel,
):
    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "female"

    email = models.EmailField(max_length=120, unique=True)

    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=2555,
        null=True,
        blank=True,
    )
    is_staff = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to="media/Y%m%d",
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=10,
        choices=Gender,
        default=None,
        null=True,
        blank=True,
    )

    birthday = models.DateField(
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
