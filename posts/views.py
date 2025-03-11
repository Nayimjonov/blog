from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TagSerializer, PostSerializer
from .models import Tag, Post
from .pagination import TagListPagination, PostListPagination


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TagListPagination

class PostListByTagView(APIView):
    def get(self, request, slug):
        try:
            tag = Tag.objects.get(slug=slug)
        except Tag.DoesNotExist as ex:
            return Response({
                'error': 'Tag Not Found'
            }, status=404)
        serializer = PostSerializer(tag.posts, many=True)
        return Response(serializer.data)

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostListPagination

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'