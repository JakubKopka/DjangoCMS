# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class PrivateMessages(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tytuł wiadomości")
    content = models.TextField(verbose_name="Treść")
    viewed = models.BooleanField(default=False)
    sender = models.ForeignKey(User, related_name="Nadawca", on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name="Odbiorca", on_delete=models.CASCADE)
    published = models.DateTimeField(verbose_name="Data wysłania", default=None)

    class Meta:
        verbose_name = "Wiadomość"
        verbose_name_plural = "Wiadomości"

        def __str__(self):
            return str(self.title)

    def __unicode__(self):
        return self.title


@receiver(post_save, sender=User)
def send_welcome_message(sender, **kwargs):
    if kwargs.get('created', False):
        recipient = User.objects.get(id=1)
        PrivateMessages.objects.create(recipient=kwargs.get('instance'),
                                       title="Witamy",
                                       content="Treść",
                                       sender=recipient,
                                       published=datetime.datetime.now(),
                                       )
