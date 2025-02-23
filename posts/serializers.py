from rest_framework import serializers
from authors.serializers import AuthorModelSerializer
from .models import Post, Tag
from django.utils.text import slugify


class TagModelSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug', 'post_count')

    def get_post_count(self, obj):
        return obj.posts.count()

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)


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
