from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.urls import reverse

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

def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comment = request.POST["comment"]
    c = Comment(article_ID=article, heading=request.POST["heading"], text=request.POST["comment"], 
                pub_date=datetime.now())
    c.save()

    comments = article.comment_set.all()

    return HttpResponseRedirect(reverse("article", args=(article.id,)))