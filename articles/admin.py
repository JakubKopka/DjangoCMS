# -*- coding: utf-8 -*-
from django.contrib import admin
from articles.models import *


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    search_fields = ['title', 'content']

admin.site.register(Article, ArticlesAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'content', 'published')
    list_filter = ('published',)

admin.site.register(Comment, CommentAdmin)


