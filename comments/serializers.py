from rest_framework import serializers
from .models import Comment


class CommentModelSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment', 'post', 'replies')

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentModelSerializer(obj.replies.all(), many=True).data
        return []
