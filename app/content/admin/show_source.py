from django.contrib import admin
from content.models import ShowSource
from django.utils.safestring import mark_safe


class ShowSourceTabularInline(admin.TabularInline):
    model = ShowSource
    extra = 1


@admin.register(ShowSource)
class ShowSourceAdmin(admin.ModelAdmin):
    list_display = ["show", "get_download_link", "source"]
    list_filter = ["source"]
    list_per_page = 10

    def get_download_link(self, obj):
        return mark_safe(
            f"<a href='{obj.download_link}' target='_blank'>{obj.download_link}</a>"
        )

    get_download_link.short_description = "download_link"
