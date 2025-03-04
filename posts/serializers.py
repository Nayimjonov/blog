from rest_framework import serializers
from django.utils.text import slugify
from authors.serializers import AuthorModelSerializer
from categories.serializers import CategoryModelSerializer
from authors.models import Author
from categories.models import Category
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
    status = serializers.ChoiceField(choices=Post.STATUS_CHOICES)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'content', 'status',
            'created_at', 'updated_at', 'author', 'category',
            'tags', 'comments_count'
        )

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        category_data = validated_data.pop('category', {})
        author_data = validated_data.pop('author', {})

        author, _ = Author.objects.get_or_create(**author_data)
        validated_data['author'] = author

        category, _ = Category.objects.get_or_create(**category_data)
        validated_data['category'] = category

        if 'slug' not in validated_data:
            validated_data['slug'] = slugify(validated_data['title'])
        post = Post.objects.create(**validated_data)

        for tag_data in tags_data:
            tag_name = tag_data.get('name')
            tag_slug = slugify(tag_name)

            tag, _ = Tag.objects.get_or_create(slug=tag_slug, defaults={'name': tag_name})
            post.tags.add(tag)
        return post
