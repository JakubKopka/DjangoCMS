from django.contrib import admin
from userprofile.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Profile, ProfileAdmin)




