from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, PostForm, CommentForm
from .models import Post, Comment
import datetime
def Home_View(request):
    return render(request, "furumapp/index.html")

def default_view(request):
    return redirect('furum')  # Replace 'desired_url_name' with the name of the URL pattern you want to redirect to

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'furumapp/register.html', { 'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'furumapp/register.html', {'form': form})

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')

        form = LoginForm()
        return render(request, 'furumapp/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('home')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'furumapp/login.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')

def Posts_View(request, topic):
    if request.method == 'GET':
        form = PostForm()
        posts = Post.objects.filter(topic=topic)
        context = {"posts": posts, "topic": topic, "form": form}
        return render(request, "furumapp/postsview.html", context)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.datetime.now()
            post.user = request.user
            post.topic = topic
            post.comment_count = 0
            post.save()
            messages.success(request, 'Post successful.')
            return redirect('posts', topic=topic)
        else:
            posts = Post.objects.filter(topic=topic)
            context = {"posts": posts, "topic": topic, "form": form}
            return render(request, 'furumapp/postsview.html', context)

def Post_Details(request, post_id):
    if request.method == 'GET':
        form = CommentForm()
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        context = {"post": post, "comments": comments, "form": form}
        return render(request, "furumapp/postdetails.html", context)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        post = get_object_or_404(Post, id=post_id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.timestamp = datetime.datetime.now()
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment successful.')
            post.comment_count = post.comment_count + 1
            post.save()
            return redirect('postdetails', post_id=post_id)
        else:
            comments = Comment.objects.filter(post=post)
            context = {"post": post, "comments": comments, "form": form}
            return render(request, 'furumapp/postdetails.html', context)

def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        comment.delete()
        post.comment_count = post.comment_count - 1
        post.save()
        return redirect('postdetails', post_id)

    return render(request, 'postdetails.html', {'comment':comment})

def post_delete(request, topic, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()

    return redirect('posts', topic=topic)