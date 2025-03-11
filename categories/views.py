from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer
from .models import Category
from .pagination import CategoryListPagination


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryListPagination