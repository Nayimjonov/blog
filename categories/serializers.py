from rest_framework import serializers
from .models import Category
from django.utils.text import slugify


class CategoryModelSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description')

    def create(self, validated_data):
        if 'slug' not in validated_data:
            validated_data['slug'] = slugify(validated_data['name'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        if 'name' in validated_data:
            instance.slug = slugify(validated_data['name'])

        instance.save()
        return instance