from django.urls import path

from . import views

app_name = "articles"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:article_id>", views.article, name="article"),
    path("<int:article_id>/comment/", views.comment, name="comment"),
    path(
        "<int:article_id>/<str:tag>",
        views.index_filtered,
        name="tag_filter",
    ),
]
