from rest_framework import serializers
from authors.serializers import AuthorModelSerializer
from .models import Post, Tag
from django.utils.text import slugify
from categories.serializers import CategoryModelSerializer


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
    category = CategoryModelSerializer()
    tags = TagModelSerializer(many=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content', 'status', 'created_at', 'updated_at', 'author', 'category', 'tags', 'comments_count')

    def get_comments_count(self, obj):
        return obj.comments.count()

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)