from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.urls import reverse

from .models import Article, Article_Tag, Comment, Tag

def index(request):
    filt, filts = filterer(request)
    articles, sort, sort_options = sorter(request)

    context = {
        "articles_list": articles, 
        "sort_order": sort, 
        "sort_options": sort_options,
        "filt": filt,
        "filters": filts
    }
    
    return render(request, "articles/index.html", context)

def sorter(request):
    if order:=request.GET.get('article-sort'):
        sort = order
        if order == "Newest":
            articles = Article.objects.order_by("-pub_date")
        elif order == "Oldest":
            articles = Article.objects.order_by("pub_date")
        elif order == "A-Z":
            articles = Article.objects.order_by("heading")
        elif order == "Z-A":
            articles = Article.objects.order_by("-heading")
        elif order == "Most Views":
            articles = Article.objects.order_by("-view_count")
        else:
            articles = Article.objects.order_by("view_count")
    else:
        articles = Article.objects.order_by("-pub_date")
        sort = "Newest"

    sort_options = ('Newest', 'Oldest', 'A-Z', 'Z-A', 'Most Views', 'Least Views')

    return (articles, sort, sort_options)

def filterer(request):
    filter_options = Tag.objects.all()
    
    filt = request.GET.get('article-filter')

    return (filt, filter_options)

def home_view(request):
    return render(request, "home.html", {})


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    comments = article.comment_set.all().order_by('-pub_date')

    return render(request, "articles/article.html", {"article": article, "comments":comments})

def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comment = request.POST["comment"]
    heading = request.POST["heading"]

    c = Comment(article_ID=article, heading=heading, text=comment, pub_date=datetime.now())
    c.save()

    return HttpResponseRedirect(reverse("articles:article", args=(article.id,)))
