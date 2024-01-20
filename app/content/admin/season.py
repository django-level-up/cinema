from django.contrib import admin
from content.models import Season
from .season_source import SeasonSourceTabularInline


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "short_description",
        "duration",
    )
    list_per_page = 10
    inlines = [SeasonSourceTabularInline]
    exclude = ("sources",)
    # prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (
            "Basic",
            {
                "fields": (
                    "title",
                    "description",
                    "show",
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
