from rest_framework import serializers
from content.models import Episode, EpisodeSource
from .episode_source import EpisodeSourceSerializer

class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = (
            "id",
            "title",
            "description",
            "duration",
        )

class EpisodeDetailSerializer(serializers.ModelSerializer):
    episode_sources = serializers.SerializerMethodField()

    def get_episode_sources(self, obj):
        sources = EpisodeSource.objects.filter(episode=obj)
        return EpisodeSourceSerializer(sources, many=True).data

    class Meta:
        model = Episode
        fields = "__all__"
