from django.urls import path
from .views import AuthorAPIView, AuthorDetailView


app_name='authors'
urlpatterns=[
    path('authors/', AuthorAPIView.as_view(), name='list'),
    path('create/', AuthorDetailView.as_view(), name='create'),

]
