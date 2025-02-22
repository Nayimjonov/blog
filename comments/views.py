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

    def post(self, request):
        serializer = CommentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except  Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentModelSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentModelSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











