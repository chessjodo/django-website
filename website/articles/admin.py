from django.contrib import admin

from .models import *

# Register your models here.
models = (Comment, Tag)
for m in models:
    admin.site.register(m)


class ArticleAdmin(admin.ModelAdmin):
    exclude = ("view_count",)


admin.site.register(Article, ArticleAdmin)
