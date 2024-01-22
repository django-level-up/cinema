from django.contrib import admin
from content.models import EpisodeSource
from django.utils.safestring import mark_safe


class EpisodeSourceInline(admin.StackedInline):
    model = EpisodeSource
    extra = 1


@admin.register(EpisodeSource)
class EpisodeSourceAdmin(admin.ModelAdmin):
    list_display = ["get_download_link", "source"]
    list_filter = ["source"]
    list_per_page = 10

    def get_download_link(self, obj):
        return mark_safe(
            f"<a href='{obj.download_link}' target='_blank'>{obj.download_link}</a>"
        )

    get_download_link.short_description = "download_link"
