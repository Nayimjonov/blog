from rest_framework import serializers
from .models import Comment


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id', 'author_name', 'author_email', 'content',
            'created_at', 'parent_comment', 'post'
        )
