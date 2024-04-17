from django.db import models
from django_resized import ResizedImageField


class Author_Manager(models.Manager):
    def use_nat_keys(self, name):
        return self.get(name=name)


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio_text = models.CharField(max_length=200)
    bio_edit = models.DateTimeField("info date edited")
    picture = ResizedImageField(
        size=[300, 300],
        quality=75,
        upload_to="author_pictures/",
        force_format="WEBP",
        blank=True,
    )

    def __str__(self):
        return self.name


class Author_Articles(models.Model):
    from articles.models import Article

    author_id = models.OneToOneField(Author, on_delete=models.CASCADE)
    article_id = models.OneToOneField(Article, on_delete=models.CASCADE)
