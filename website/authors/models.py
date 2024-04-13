from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    bio_text = models.CharField(max_length=200)
    bio_edit = models.DateTimeField("info date edited")


# Create your models here.
