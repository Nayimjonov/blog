from rest_framework import serializers
from .models import Comment


class CommentModelSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    author_email = serializers.EmailField(validators=[])

    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment', 'post', 'replies')

    def get_replies(self, obj):
        replies = Comment.objects.filter(parent_comment=obj.id)
        return CommentModelSerializer(replies, many=True).data

    def validate(self, data):
        if data.get('parent_comment') and Comment.objects.filter(parent_comment=data['parent_comment']).count() >= 3:
            raise serializers.ValidationError("Komment darajasi 3 dan oshmasligi kerak.")
        return data