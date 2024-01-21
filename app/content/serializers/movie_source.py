from rest_framework import serializers
from content.models import MovieSource


class MovieSourceSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = MovieSource
        fields = [
            "title",
            "download_link",
            "kinopoisk_link",
            "imdb_link",
            "tmdb_link",
            "watch_link",
            "valid_source",
        ]

    def get_title(self, obj):
        return obj.source.title if obj.source else None
