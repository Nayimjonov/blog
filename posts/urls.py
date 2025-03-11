from django.urls import path
from . import views

urlpatterns = [
    path('tags/', views.TagListView.as_view(), name='tags_list'),
    path('tags/<slug:slug>/posts/', views.PostListByTagView.as_view(), name='post_by_tag'),
    path('posts/', views.PostListCreateView.as_view(), name='post_list'),
    path('posts/<slug:slug>/', views.PostRetrieveUpdateDestroyView.as_view(), name='post_detail'),
]