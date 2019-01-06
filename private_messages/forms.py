from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from private_messages.models import PrivateMessages


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessages
        fields = ('__all__')
