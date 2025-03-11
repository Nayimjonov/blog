from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/comments/', views.CommentListCreateView.as_view(), name='comment_list'),
]