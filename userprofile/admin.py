# -*- coding: utf-8 -*-
from django.contrib import admin
from userprofile.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    # search_fields = ['',]


admin.site.register(Profile, ProfileAdmin)




