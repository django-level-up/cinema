from django.contrib import admin
from content.models import Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    list_per_page = 10
    prepopulated_fields = {"slug": ("title",)}
