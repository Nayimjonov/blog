from rest_framework import serializers
from .models import Category
from django.utils.text import slugify



class CategoryModelSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'post_count')

    def get_post_count(self, obj):
        return obj.posts.count()

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)