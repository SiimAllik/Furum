from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    text = forms.CharField(max_length=10000)

    class Meta:
        model = Post
        fields = ['title', 'text']

class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=10000)

    class Meta:
        model = Comment
        fields = ['text']