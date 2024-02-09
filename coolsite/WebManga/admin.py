from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import *


class MangaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'manga', 'time_create', 'time_update')
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


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'sender')
    list_display_links = ('id', 'message',)
    search_fields = ('message',)


# class ProfileUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'get_html_image', 'slug')
#     list_display_links = ('id', 'user',)
#     search_fields = ('user',)

#     def get_html_image(self, object):
#         if object.photo:
#             return mark_safe(f"<img src='{object.photo.url}' width=50>")

#     get_html_image.short_description = 'Фото пользователя'


admin.site.register(Manga, MangaAdmin)
admin.site.register(MangaImage, MangaImagesAdmin)
admin.site.register(Category, CategoryAdmnin)
admin.site.register(Message, MessageAdmin)
admin.site.register(User, UserAdmin)