from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentModelSerializer


class CommentAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentModelSerializer(comments, many=True)
        return Response(serializer.data)



