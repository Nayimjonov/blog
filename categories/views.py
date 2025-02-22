from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategoryModelSerializer


class CategoryAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

