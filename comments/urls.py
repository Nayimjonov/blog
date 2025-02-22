from django.urls import path
from .views import CommentAPIView, CommentDetailAPIView


app_name='comments'

urlpatterns=[
    path('comments/', CommentAPIView.as_view(), name='list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='create'),
]