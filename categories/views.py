from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategoryModelSerializer


class CategoryAPIView(APIView):
    def get(self, request):
