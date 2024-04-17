from django.db.models import Count, Max, Min
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Author, Author_Articles


def index(request):
    authors = Author.objects.all()
    if sort := request.GET.get("sort"):
        if sort == "A-Z":
            authors = authors.order_by("name")
        elif sort == "Z-A":
            authors = authors.order_by("-name")
        elif sort == "Most Articles":
            authors = authors.annotate(
                article_count=Count("article")
            ).order_by("-article_count")
        elif sort == "Least Articles":
            authors = authors.annotate(
                article_count=Count("article")
            ).order_by("article_count")
        elif sort == "Most Recently Published":
            authors = authors.annotate(
                max_pub_date=Max("article__pub_date")
            ).order_by("-max_pub_date")
        else:
            authors = authors.annotate(
                min_pub_date=Min("article__pub_date")
            ).order_by("min_pub_date")
    else:
        authors = authors.order_by("name")
        sort = "A-Z"
    sort_options = (
        "A-Z",
        "Z-A",
        "Most Articles",
        "Least Articles",
        "Most Recently Published",
        "Least Recently Published",
    )
    context = {
        "authors_lst": authors,
        "sort_p": sort,
        "sort_options": sort_options,
    }
    return render(request, "index.html", context)


def author(request, author_id):
    from articles.models import Article

    author = get_object_or_404(Author, pk=author_id)
    articles = Article.objects.filter(author=author)
    context = {
        "author": author,
        "articles": articles,
    }
    return render(request, "author.html", context)


# Create your views here.
