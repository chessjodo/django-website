from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("This is the authors index.")


# Create your views here.
