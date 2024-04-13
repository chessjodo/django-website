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


class Comment(models.Model):
    article_ID = models.ForeignKey(Article, on_delete=models.CASCADE)
    heading = models.CharField(max_length=150)
    text = models.TextField(max_length=5000)
    pub_date = models.DateTimeField()


class Tag(models.Model):
    text = models.CharField(max_length=50)
    count = models.IntegerField(default=0)


class Article_Tag(models.Model):
    article_ID = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag_ID = models.ForeignKey(Tag, on_delete=models.CASCADE)
