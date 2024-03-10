from django.contrib import admin

from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'sender')
    list_display_links = ('id', 'message',)
    search_fields = ('message',)


admin.site.register(Comment, CommentAdmin)