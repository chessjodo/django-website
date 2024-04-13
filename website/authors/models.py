from articles.models import Article
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio_text = models.CharField(max_length=200)
    bio_edit = models.DateTimeField("info date edited")


class Author_Articles(models.Model):
    author_id = models.OneToOneField(Author, on_delete=models.CASCADE)
    article_id = models.OneToOneField(Article, on_delete=models.CASCADE)


# Create your models here.
