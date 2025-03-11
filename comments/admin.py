from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'parent_comment', 'author_name', 'author_email', 'created_at')
    search_fields = ('content',)
    list_filter = ('post', 'parent_comment', 'created_at')