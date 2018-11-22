import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from articles.forms import CommentForm, AddArticleForm
from articles.models import *

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from DjangoCMS.render import Render

def articles(request):
    data = {'articles': Article.objects.all().order_by('-id')}
    data['title'] = "Artykuły"
    return render(request, 'articles.html', data)


@csrf_protect
def article(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()
    if request.POST:
        data = request.POST.copy()
        data['user'] = request.user.id
        data['article'] = article.id
        data['published'] = datetime.datetime.now()
        form = CommentForm(data)
        if form.is_valid():
            form.save()
            form = CommentForm()

    data = {}
    data['title'] = article.title
    data['article'] = article
    data['form'] = form
    return render(request, 'article.html', data)


@login_required
def add_article(request):
    data = {}
    data['title'] = "Dodawanie artykułu"
    form = AddArticleForm()
    if request.POST:
        data = request.POST.copy()
        data['user'] = request.user.id
        data['published'] = datetime.datetime.now()
        form = AddArticleForm(data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    data['form'] = form
    return render(request, 'addArticle.html', data)


def show_article_pdf(request, id):
        a = Article.objects.get(id=id)
        today = datetime.datetime.now()
        params = {
            'title' : a.title,
            'today': today,
            'article': a,
            'request': request
        }
        return Render.render('article_pdf.html', params)
