from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class MangaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published', 'rating', 'years_of_release', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'manga', 'time_create', 'time_update', 'rating', 'years_of_release', 'author', 'transfer_status')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'


class MangaImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_html_image', 'description', 'time_create']
    list_display_links = ['id', 'time_create']
    search_fields = ['id', 'description']
    list_filter = ['description',]
    fields = ['image', 'description', 'time_create']
    readonly_fields = ['time_create',]

    def get_html_image(self, object):
         if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_image.short_description = 'Миниатюра манги'


class CategoryAdmnin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Manga, MangaAdmin)
admin.site.register(MangaImage, MangaImagesAdmin)
admin.site.register(Category, CategoryAdmnin)