from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {"articles": articles})


def article_details(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, "blog/details.html", {"article": article})


def article_edit(request, article_id=0):
    if int(article_id) > 0:
        article = models.Article.objects.get(pk=article_id)
    else:
        article = models.Article()
        article.pk = 0
        article.title = ""
        article.content = ""

    return render(request, 'blog/edit.html', {"article": article})


def article_submit(request):
    article_id = request.POST.get('id', '0')
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')

    if int(article_id) == 0:
        models.Article.objects.create(title=title, content=content)
        return HttpResponseRedirect('/blog/index')
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return HttpResponseRedirect('/blog/details/' + article_id)

