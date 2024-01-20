from django.core.management.base import BaseCommand
from content.task import fibonacci


class Command(BaseCommand):
    help = "Import movie information from IMDb"

    def handle(self, *args, **options):
        fibonacci.delay(10)

