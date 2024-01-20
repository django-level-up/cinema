from django.contrib.auth.models import BaseUserManager
from typing import Optional, Dict


class UserManager(BaseUserManager):

    """Crate simple user"""

    def create_user(self, email: str, password: Optional[str] = None, **kwargs: Dict):
        if not email:
            raise ValueError("User must be provided by email!")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    """Crate superuser """

    def create_superuser(
        self, email: str, password: Optional[str] = None, **kwargs: Dict
    ):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)
        return self.create_user(
            email=email,
            password=password,
            **kwargs,
        )
