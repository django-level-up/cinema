from django.contrib import admin
from content.models import ShowSource
from django.utils.html import format_html


class ShowSourceInline(admin.StackedInline):
    model = ShowSource
    extra = 1


@admin.register(ShowSource)
class ShowSourceAdmin(admin.ModelAdmin):
    list_display = [
        "show",
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
