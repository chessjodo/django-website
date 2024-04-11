from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the Articles index.")


def home_view(request):
    return render(request, "home.html", {})
