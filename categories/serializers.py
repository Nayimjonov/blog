from rest_framework import serializers
from .models import Category
from django.utils.text import slugify


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description')

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)