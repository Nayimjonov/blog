from rest_framework import serializers
from .models import Post
from authors.serializers import AuthorSerializer
from categories.serializers import CategorySerializer


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    slug = serializers.SlugField()
    post_count = serializers.SerializerMethodField()

    def get_post_count(self, obj):
        return obj.posts.count()

class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content', 'author', 'category', 'tags', 'created_at', 'updated_at', 'status', 'comments_count')

    def get_comments_count(self, instance):
        return instance.comments.count()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = AuthorSerializer(instance.author).data
        data['category'] = CategorySerializer(instance.category).data
        data['tags'] = TagSerializer(instance.tags, many=True).data
        return data