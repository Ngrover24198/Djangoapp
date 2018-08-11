from django import forms

from . import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput())

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = '__all__'
        

