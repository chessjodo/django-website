from django.http import HttpResponse
from django.shortcuts import render

from .models import Article, Article_Tag, Comment, Tag


def index(request):
    articles = Article.objects.order_by("-pub_date")
    context = {"articles_list": articles}
    return render(request, "articles/index.html", context)


def home_view(request):
    return render(request, "home.html", {})


def article(request, article_id):
    response = f"You're looking at article {article_id}"
    article = Article.objects.get(id=article_id)
    article.add_view()
    article.save()
    return HttpResponse(response)
