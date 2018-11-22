import datetime

from django import forms
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf

from articles.forms import CommentForm, AddArticleForm
from articles.models import *

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

def articles(request):
    data = {'articles': Article.objects.all().order_by('-id')}
    data['title'] = "Artykuły"
    return render(request, 'articles.html', data)

# @csrf_protect
# def addComent(request, id):
#     art = Article.objects.get(id=id)
#
#     if request.POST:
#         comentForm = CommentForm(request.POST)
#         if comentForm.is_valid():
#             comment = comentForm.save(commit=False)
#             comment.published = datetime.timezone.now()
#             comment.article = art
#             comment.save()
#
#             return HttpResponseRedirect('/article/%s' % id)
#     else:
#         comment = CommentForm()
#
#     args = {}
#     args['article'] = art
#     args['form'] = comment
#
#     return render_to_response('add_comment.html', args)

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