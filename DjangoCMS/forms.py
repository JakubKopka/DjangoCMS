from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2',)
