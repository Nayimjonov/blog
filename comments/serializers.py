from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from posts.models import Post
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    post = serializers.IntegerField(write_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment', 'post', 'replies')

    def get_replies(self, instance):
        replies = instance.child.all()
        return CommentSerializer(replies, many=True).data


    def create(self, validated_data):
        try:
            post = Post.objects.get(pk=validated_data.pop('post'))
        except ObjectDoesNotExist:
            raise serializers.ValidationError({"post": "Invalid post ID"})

        return Comment.objects.create(post=post, **validated_data)