from rest_framework import serializers
from content.models import ShowSource, Show
from .show_source import ShowSourceSerializer
from .season import SeasonSerializer


class ShowSerializer(serializers.ModelSerializer):
    # show_sources = serializers.SerializerMethodField()

    # def get_show_sources(self, obj):
    #     sources = ShowSource.objects.filter(movie=obj)
    #     return ShowSourceSerializer(sources, many=True).data

    class Meta:
        model = Show
        fields = (
            "id",
            "title",
            "image",
            "imdb_rating",
            "kinopoisk_rating",
            # "show_sources",
        )


class ShowDetailSerializer(serializers.ModelSerializer):
    seasons = serializers.SerializerMethodField()
    show_sources = serializers.SerializerMethodField()

    def get_show_sources(self, obj):
        sources = ShowSource.objects.filter(show=obj)
        return ShowSourceSerializer(sources, many=True).data

    def get_seasons(self, obj):
        seasons = obj.seasons.all().values(
            "id",
            "title",
        )
        return SeasonSerializer(seasons, many=True).data

    class Meta:
        model = Show
        fields = "__all__"
