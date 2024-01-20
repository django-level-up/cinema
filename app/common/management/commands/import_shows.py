from django.core.management.base import BaseCommand
from content.models import Show
import requests


class Command(BaseCommand):
    help = "Import movies from JSON and extract names."

    def handle(self, *args, **options):
        shows = Show.objects.all()
        shows.delete()
        json_url = "https://channelsapi.s3.amazonaws.com/media/test/shows.json"
        
        try:
            response = requests.get(json_url)
            response.raise_for_status()
            data = response.json()

            if isinstance(data, list):
                names = [item.get("name") for item in data]
                self.stdout.write(self.style.SUCCESS(f"Names extracted: {names}"))

            
            for name in names:
                Show.objects.create(title=str(name))

            else:
                self.stdout.write(
                    self.style.ERROR("Invalid JSON format. Expected a list.")
                )

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
