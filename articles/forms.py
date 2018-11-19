from django import forms
from articles.models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ('user', 'content')


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'