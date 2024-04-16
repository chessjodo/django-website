from django.db.models import Count, Max, Min
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Author, Author_Articles


def index(request):
    from articles.models import Article

    articles = None

    authors = Author.objects.all()
    sort = request.GET.get("sort")
    if sort == "name_ascending":
        authors = authors.order_by("name")
    elif sort == "name_descending":
        authors = authors.order_by("-name")
    #  elif sort == "most_articles":
    #      authors = authors.annotate(article_count=Count("articles")).order_by(
    #         "-article_count"
    #    )
    # elif sort == "least_articles":
    #    authors = authors.annotate(article_count=Count("articles")).order_by(
    #       "article_count"
    #  )
    # elif sort == "most_recent":
    #    authors = authors.annotate(
    #       max_pub_date=Max("articles__pub_date")
    #  ).order_by("-max_pub_date")
    #  elif sort == "least_recent":
    #     authors = authors.annotate(
    #        min_pub_date=Min("articles__pub_date")
    #   ).order_by("min_pub_date")
    else:
        authors = authors.order_by("name")
        sort = "name_ascending"
    #  if "author_id" in request.GET:
    #     author_id = request.GET.get("author_id")
    #    author = get_object_or_404(Author, pk=author_id)
    #     articles = Article.objects.filter(author=author)
    context = {
        "authors_lst": authors,
        "sort_p": sort,
        #    "articles": articles,
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
