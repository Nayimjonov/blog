from rest_framework import serializers
from .models import Author


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'bio')

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Muallif ismi kamida 2 ta belgidan iborat bo'lishi kerak.")
        return value

    def validate_email(self, value):
        if Author.objects.filter(email=value).exists():
            raise serializers.ValidationError("Bu email manzil bilan ro'yxatdan o'tilgan.")
        return value

    def validate_bio(self, value):
        if value and len(value.split()) < 5:
            raise serializers.ValidationError("Biografiya kamida 5 ta so'zdan iborat bo'lishi kerak.")
        return value