from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Author, Author_Articles


def index(request):
    authors = Author.objects.order_by("name")
    context = {"authors_lst": authors}
    return render(request, "index.html", context)


def author(request, author_id):
    from articles.models import Article

    author = get_object_or_404(Author, pk=author_id)
    articles = Article.objects.filter(author=author)
    context = {"author": author, "articles": articles}
    return render(request, "author.html", context)


# Create your views here.
