from django.db import models

class Tag(models.Model):
    text = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class Article(models.Model):
    heading = models.CharField(max_length=150)
    text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    picture = models.ImageField(
        upload_to="article_pictures/",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
    )
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(
        "authors.Author", on_delete=models.CASCADE, default=1
    )

    def add_view(self):
        self.view_count += 1
        print("add view")

    def __str__(self):
        return self.heading


class Comment(models.Model):
    article_ID = models.ForeignKey(Article, on_delete=models.CASCADE)
    heading = models.CharField(max_length=150)
    text = models.TextField(max_length=5000)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.heading

