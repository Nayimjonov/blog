from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author
from .serializers import AuthorModelSerializer


class AuthorAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serialize = AuthorModelSerializer(authors, many=True)
        return Response(serialize.data)