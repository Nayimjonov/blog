from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Tag
from .serializers import PostModelSerializer


class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data)
