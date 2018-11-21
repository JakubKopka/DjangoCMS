# -*- coding: utf-8 -*-
from django.contrib import admin
from private_messages.models import *


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'title')
    search_fields = ['recipient', 'sender', 'title']


admin.site.register(PrivateMessages, MessagesAdmin)



