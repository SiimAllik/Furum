from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, ValidationError
from .models import Post, Comment


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=65,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "name":"username",
                "placeholder":"username"
            }
        )
    )
    password = forms.CharField(
        max_length=65,
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control mt-2",
                "name":"password",
                "placeholder":"password"
            }
        )
    )

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'class': 'form-control'
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'youremail@example.com',
                'class': 'form-control my-2'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'confirm password',
                'class': 'form-control mt-2'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "name":"title",
                "placeholder":"Post title"
            }
        )
    )
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control my-2",
                "name":"text",
                "placeholder":"What's on your mind?",
                "rows":4
            }
        )
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "class":"form-control mb-2"
            }
        )
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'image']

class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control my-2",
                "name":"text",
                "placeholder":"What's on your mind?",
                "rows":4}
        )
    )

    class Meta:
        model = Comment
        fields = ['text']