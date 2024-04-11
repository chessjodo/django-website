from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=200)
    # author = models.ForeignKey(Author)
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField("date published")
