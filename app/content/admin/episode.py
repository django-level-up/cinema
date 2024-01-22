from django.contrib import admin
from content.models import Episode
from .episode_source import EpisodeSourceInline


class EpisodeInline(admin.StackedInline):
    model = Episode
    extra = 1


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "short_description",
        "duration",
    )
    list_per_page = 10
    inlines = [EpisodeSourceInline]
    exclude = ("sources",)
    # prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (
            "Basic",
            {
                "fields": (
                    "title",
                    "description",
                )
            },
        ),
    )

    def short_description(self, obj):
        return (
            obj.description[:40] + "..."
            if len(str(obj.description)) > 40
            else obj.description
        )

    short_description.short_description = "description"
