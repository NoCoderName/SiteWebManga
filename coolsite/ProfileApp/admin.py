from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_html_image', 'user')
    list_display_links = ('user',)
    # filter_horizontal = ('read',)

    def get_html_image(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_image.short_description = 'Фото пользователя'


admin.site.register(Profile, ProfileAdmin)