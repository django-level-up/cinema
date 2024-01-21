from django.contrib import admin
from django.utils.html import format_html
from content.models import MovieSource


class MovieSourceInline(admin.StackedInline):
    model = MovieSource
    extra = 1


@admin.register(MovieSource)
class MovieSourceAdmin(admin.ModelAdmin):
    list_display = [
        "movie",
        "get_watch_link",
        "source",
        "valid_source",
    ]
    list_filter = ["source"]
    list_per_page = 10

    def get_watch_link(self, obj):
        return (
            format_html(
                '<a href="{}" style="color:blue" target="_blank">Watch/Download</a>',
                obj.watch_link,
            )
            if obj.watch_link
            else format_html("<p>-</p>")
        )

    get_watch_link.short_description = "Watch Link"
