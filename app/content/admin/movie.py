from django.contrib import admin
from content.models import Movie, Source, MovieSource
from .movie_source import MovieSourceInline
from django.utils.html import format_html
from django.utils.safestring import mark_safe


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_image",
        "short_description",
        "duration",
        "imdb_rating",
        "tmdb_rating",
        "kinopoisk_rating",
        "get_play_link_imdb",
        "get_play_link_tmdb",
        "get_play_link_kp",
        "get_watch_link",
        "get_valid_source",
        "release_date",
    )
    list_per_page = 10
    inlines = [MovieSourceInline]
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
                    "tmdb_rating",
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

    def get_play_link_imdb(self, obj):
        imdb_instance = Source.objects.filter(slug="imdb").first()
        imdb = MovieSource.objects.filter(movie=obj, source=imdb_instance).first()
        if imdb:
            return format_html(
                f'<a href="{imdb.imdb_link}" target="_blank" style="color: blue;" >Click</a>',
            )
        return mark_safe("<p>No imdb link</p>")

    get_play_link_imdb.short_description = "IMDB-LINK"

    def get_play_link_tmdb(self, obj):
        tmdb_instance = Source.objects.filter(slug="tmdb").first()
        tmdb = MovieSource.objects.filter(movie=obj, source=tmdb_instance).first()
        if tmdb:
            return format_html(
                f'<a href="{tmdb.tmdb_link}" target="_blank" style="color: blue;">Click</a>',
            )
        return mark_safe("<p>No tmdb link</p>")

    def get_play_link_kp(self, obj):
        tmdb_instance = Source.objects.filter(slug="kinopoisk").first()
        tmdb = MovieSource.objects.filter(movie=obj, source=tmdb_instance).first()
        if tmdb:
            return format_html(
                f'<a href="{tmdb.kinopoisk_link}" target="_blank" style="color: blue;">Click</a>',
            )
        return mark_safe("<p>No kps link</p>")

    def get_watch_link(self, obj):
        kp_instance = Source.objects.filter(slug="kinopoisk").first()
        kp = MovieSource.objects.filter(movie=obj, source=kp_instance).first()
        if kp:
            return format_html(
                f'<a href="{kp.watch_link}" target="_blank" style="color: blue;" >Watch/Download</a>',
            )
        return mark_safe("<p>No watch link</p>")

    def get_valid_source(self, obj):
        kp_instance = Source.objects.filter(slug="kinopoisk").first()
        kp = MovieSource.objects.filter(movie=obj, source=kp_instance).first()
        if kp:
            return kp.valid_source
        return False

    get_play_link_imdb.short_description = "IMDB-LINK"
    get_play_link_tmdb.short_description = "TMDB-LINK"
    get_play_link_kp.short_description = "KP-LINK"
    get_watch_link.short_description = "WATCH-LINK"
    get_valid_source.short_description = "VALID-SOURCE"
