from django.urls import path
from private_messages.views import *

urlpatterns = [
    path('', messages),
    path('delete/<int:id>/', delete_messages),
    path('show/<int:id>/', show_messages),
    path('send_message/', send_message)
]