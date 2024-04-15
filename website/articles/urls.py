from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:article_id>", views.article, name="article"),
    path("<int:article_id>/comment/", views.comment, name="comment")
]
