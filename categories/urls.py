from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView


app_name='categories'

urlpatterns=[
    path('categories/', CategoryAPIView.as_view(), name='list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='create'),
]