from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Post
from .pagination import CommentListPagination
from .serializers import CommentSerializer


class CommentListCreateView(APIView):
    pagination_class = CommentListPagination

    def get_object(self, slug):
        try:
            post = Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            return Response({'error': 'Post Not Found'}, status=404)
        return post

    def get(self, request, slug):
        post = self.get_object(slug)
        if isinstance(post, Response):
            return post

        comments = post.comments.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(comments, request)
        serializer = CommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, slug):
        post = self.get_object(slug)
        if isinstance(post, Response):
            return post

        data = request.data.copy()
        data['post'] = post.id

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)