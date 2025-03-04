from rest_framework import serializers
from django.utils.text import slugify
from authors.serializers import AuthorModelSerializer
from categories.serializers import CategoryModelSerializer
from .models import Post, Tag


class TagModelSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug', 'post_count')

    def get_post_count(self, obj):
        return obj.posts.count()

    def create(self, validated_data):
        if 'slug' not in validated_data:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        if 'name' in validated_data:
            instance.slug = slugify(validated_data['name'])
        instance.save()
        return instance

class PostModelSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)
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
        if 'slug' not in validated_data:
            validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        if 'title' in validated_data:
            instance.slug = slugify(validated_data['title'])
        instance.save()
        return instance
