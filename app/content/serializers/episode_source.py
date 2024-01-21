from rest_framework import serializers
from content.models import EpisodeSource

class EpisodeSourceSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = EpisodeSource
        fields = [
            "title",
            "download_link",
            "kinopoisk_link",
            "imdb_link",
            "valid_source",
        ]

    def get_title(self, obj):
        return obj.source.title if obj.source else None
