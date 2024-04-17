from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Article, Comment, Tag
from authors.models import Author
from .forms import CommentForm

def home_view(request):
    """The home view of the website, displays 3 articles and allows articles to be 
    sorted and filtered, also displays authors"""
    
    # sort and filter articles by user given parameters
    articles, sort, sort_options = sorter(request)
    filtered, filt, filts = filterer(request, articles)
    authors = Author.objects.order_by("name")

    context = {
        "articles_list": filtered[:3],
        "sort_order": sort,
        "sort_options": sort_options,
        "filt": filt,
        "filters": filts,
        "authors": authors
    }

    return render(request, "articles/home.html", context)

def index(request):
    """The articles view, displays all articles and allows articles to be sorted 
    and filtered"""
    articles, sort, sort_options = sorter(request)
    filtered, filt, filts = filterer(request, articles)

    context = {
        "articles_list": filtered,
        "sort_order": sort,
        "sort_options": sort_options,
        "filt": filt,
        "filters": filts,
    }

    return render(request, "articles/index.html", context)


def index_filtered(request, article_id, tag):
    """View to handle tag being clicked on article page"""

    url = (
        reverse("articles:index")
        + f"?article-filter={tag}&article-sort=Newest"
    )
    return redirect(url)


def sorter(request):
    """helper function that sorts articles, returns a sorted list, the sorting parameter
    and all sort options"""

    if order := request.GET.get("article-sort"):
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

    sort_options = (
        "Newest",
        "Oldest",
        "A-Z",
        "Z-A",
        "Most Views",
        "Least Views",
    )

    return (articles, sort, sort_options)


def filterer(request, articles):
    """filtering function that filters articles, returns a filtered list, the filtering parameter
    and all filter options"""

    filter_options = Tag.objects.all()
    if request.GET.get("article-filter") == "None":
        filt = "None"
        filtered = articles
    elif filt := request.GET.get("article-filter"):
        filtered = articles.filter(tags=Tag.objects.get(text=filt))
    else:
        filt = "None"
        filtered = articles

    return (filtered, filt, filter_options)



def article(request, article_id):
    """The article view, adds one to the view counter when the view is called"""

    article = get_object_or_404(Article, pk=article_id)
    article.add_view()
    article.save()

    # get comments and sort them
    comments = article.comment_set.all().order_by("-pub_date")
    
    #get tag text
    pretags = article.tags.all()
    tags = [item.text for item in pretags]
    return render(
        request,
        "articles/article.html",
        {"article": article, "comments": comments, "tags": tags, "form": CommentForm()},
    )


def comment(request, article_id):
    """view to handle user commenting"""

    #get article and comment
    article = get_object_or_404(Article, pk=article_id)
    comment = request.POST["comment"]
    heading = request.POST["heading"]

    #save comment
    c = Comment(
        article_ID=article,
        heading=heading,
        text=comment,
        pub_date=datetime.now(),
    )
    c.save()

    #go back to article
    return HttpResponseRedirect(
        reverse("articles:article", args=(article.id,))
    )
