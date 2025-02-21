from django.db import models

from authors.models import Author
from categories.models import Category
from tags.models import Tag


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    status = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

