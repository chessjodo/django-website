from django.db import models


class Article(models.Model):
    heading = models.CharField(max_length=150)
    text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField()
    picture = models.ImageField(
        upload_to="article_pictures/",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
    )
    view_count = models.IntegerField(default=0)
