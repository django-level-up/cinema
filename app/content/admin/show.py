from django.contrib import admin
from content.models import Show
from .show_source import ShowSourceTabularInline
from django.utils.html import format_html
from django.utils.safestring import mark_safe


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_image",
        "short_description",
        "imdb_rating",
        "kinopoisk_rating",
        "duration",
        "release_date",
    )
    list_per_page = 10
    inlines = [ShowSourceTabularInline]
    exclude = ("sources",)
    # prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (
            "Basic",
            {
                "fields": (
                    "title",
                    "description",
                    "keywords",
                    "imdb_rating",
                    "kinopoisk_rating",
                )
            },
        ),
        (
            "Images",
            {
                "fields": (
                    "image",
                    "bg_image",
                ),
            },
        ),
        (
            "Additional Information",
            {
                "fields": (
                    "duration",
                    "release_date",
                ),
            },
        ),
    )

    def get_image(self, obj):
        if obj.image:
            image_url = obj.image
            return format_html(
                '<a href="{}" target="_blank">\
                    <img src="{}" alt="User Image" height="70"/></a>',
                image_url,
                image_url,
            )
        else:
            return mark_safe("<p>No image</p>")

    get_image.short_description = "image"

    def short_description(self, obj):
        return (
            obj.description[:40] + "..."
            if len(str(obj.description)) > 40
            else obj.description
        )

    short_description.short_description = "description"

    # def get_download_link(self, obj):
    #     imdb = MediaSource.objects.filter(movie=obj)
    #     if imdb:
    #         return format_html(
    #             '<a href="{}" target="_blank">{imdb}</a>',
    #         )
    #     return mark_safe("<p>No download link</p>")

    # get_download_link.short_description = "download_link"
