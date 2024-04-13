from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Article, Article_Tag, Comment, Tag


def index(request):
    articles = Article.objects.order_by("-pub_date")
    context = {"articles_list": articles}
    return render(request, "articles/index.html", context)


def home_view(request):
    return render(request, "home.html", {})


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "articles/article.html", {"article": article})
