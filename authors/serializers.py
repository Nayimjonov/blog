from rest_framework import serializers
from .models import Author


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'bio')