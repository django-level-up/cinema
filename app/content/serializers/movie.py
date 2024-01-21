from rest_framework import serializers
from content.models import MovieSource, Movie
from .movie_source import MovieSourceSerializer


class MovieSerializer(serializers.ModelSerializer):
    # movie_sources = serializers.SerializerMethodField()

    # def get_movie_sources(self, obj):
    #     sources = MovieSource.objects.filter(movie=obj)
    #     return MovieSourceSerializer(sources, many=True).data

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "image",
            "imdb_rating",
            "tmdb_rating",
            "kinopoisk_rating",
            # "movie_sources",
        )


class MovieDetailSerializer(serializers.ModelSerializer):
    movie_sources = serializers.SerializerMethodField()

    def get_movie_sources(self, obj):
        sources = MovieSource.objects.filter(movie=obj)
        return MovieSourceSerializer(sources, many=True).data

    class Meta:
        model = Movie
        fields = "__all__"
