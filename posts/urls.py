from django.urls import path
from .views import PostAPIView, PostDetailAPIView

app_name='posts'

urlpatterns=[
    path('posts/', PostAPIView.as_view(), name='list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='create'),
]