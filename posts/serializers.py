from rest_framework import serializers
from .models import Post


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', '')