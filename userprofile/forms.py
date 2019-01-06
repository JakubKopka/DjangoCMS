from django import forms
from userprofile.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('country', 'date_of_birth')
