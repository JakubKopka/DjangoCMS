#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models




class Article(models.Model):
    user = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="Tytuł")
    content = models.TextField(verbose_name="Zawartość")
    published = models.DateTimeField(verbose_name="Data publikacji")

    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"

        def __str__(self):
            return str(self.title)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="Artykuł", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Zawartość")
    published = models.DateTimeField(verbose_name="Data dodania")

    class Meta:
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"

        def __str__(self):
            return str(self.article)

    def __unicode__(self):
        return self.user
