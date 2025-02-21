from rest_framework import serializers
from authors.serializers import AuthorModelSerializer
from .models import Post, Tag


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')

class PostModelSerializer(serializers.ModelSerializer):
    author = AuthorModelSerializer()
    tags = TagModelSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'content', 'status',
            'created_at', 'updated_at', 'author',
            'category', 'tags'
        )
