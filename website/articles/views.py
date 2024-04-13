from django.http import HttpResponse
from django.shortcuts import render

from .models import Article, Article_Tag, Comment, Tag


def index(request):
    articles = Article.objects.order_by("-pub_date")
    context = {"articles_list": articles}
    return render(request, "articles/index.html", context)


def home_view(request):
    return render(request, "home.html", {})
