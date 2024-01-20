from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from django.contrib.auth import get_user_model
import os

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not get_user_model().objects.filter(email=email).exists():
            print(f"Creating account for {email}")

            get_user_model().objects.create_superuser(email=email, password=password)
        else:
            print("Admin account has already been initialized.")
