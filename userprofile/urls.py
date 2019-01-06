from django.urls import path
from userprofile.views import *

urlpatterns = [
    path('profile/', profile),
]
