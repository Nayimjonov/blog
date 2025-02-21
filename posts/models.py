from django.db import models

from authors.models import Author


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')

