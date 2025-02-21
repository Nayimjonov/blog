from rest_framework import serializers
from .models import Post, Tag


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'content', 'status',
            'created_at', 'updated_at', 'author',
            'category', 'tags'
        )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')