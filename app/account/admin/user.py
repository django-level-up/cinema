from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

import nested_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.utils.safestring import mark_safe


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin, nested_admin.NestedModelAdmin):
    list_display = [
        "get_image",
        "email",
    ]
    list_display_links = [
        "email",
        "get_image",
    ]
    ordering = ["email"]
    fieldsets = (
        (
            _("Data for registration".upper()),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password",
                    "gender",
                    "image",
                ),
            },
        ),
        (
            _("Privilege".upper()),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

    def get_image(self, obj):
        if obj.image:
            image_url = obj.image.url
            return format_html(
                '<a href="{}" target="_blank">\
                    <img src="{}" alt="User Image" height="70"/></a>',
                image_url,
                image_url,
            )
        else:
            return mark_safe("<p>No image</p>")

    get_image.short_description = "image"

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = verbose_name
