from django.contrib import admin

from .models import *

# Register your models here.
models = (Article, Comment, Tag, Article_Tag)
for m in models:
    admin.site.register(m)
