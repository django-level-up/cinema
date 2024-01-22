from rest_framework import serializers
from content.models import Season

# from .season_source import SeasonSourceSerializer
from .episode import EpisodeSerializer


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = (
            "id",
            "title",
            "description",
            "duration",
        )
        extra_kwargs = {
            "duration": {
                "required": False,
            },
            "description": {
                "required": False,
            },
        }


class SeasonDetailSerializer(serializers.ModelSerializer):
    season_sources = serializers.SerializerMethodField()
    episodes = serializers.SerializerMethodField()

    # def get_season_sources(self, obj):
    #     sources = SeasonSource.objects.filter(season=obj)
    #     return SeasonSourceSerializer(sources, many=True).data

    def get_episodes(self, obj):
        episodes = obj.episodes.all().values(
            "id",
            "title",
        )
        return EpisodeSerializer(episodes, many=True).data

    class Meta:
        model = Season
        fields = "__all__"
