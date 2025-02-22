from django.urls import path
from .views import AuthorAPIView, AuthorDetailAPIView


app_name='authors'
urlpatterns=[
    path('authors/', AuthorAPIView.as_view(), name='list'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='create'),

]
