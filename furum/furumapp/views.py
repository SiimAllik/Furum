from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, PostForm
from .models import Post, Comment, Topic
from django.db.models import Q
import datetime
from itertools import chain

def Home_View(request):
    topics = Topic.objects.all()
    return render(request, "furumapp/index.html", {"topics" : topics})

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
        form = LoginForm()
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'furumapp/login.html', {"form" : form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'furumapp/login.html', {"form" : form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')

def Posts_View(request, topic):
    if request.method == 'GET':
        default_data = {'image': ''}
        form = PostForm()
        posts = Post.objects.filter(topic=topic)
        context = {"posts": posts, "topic": topic, "form":form}
        return render(request, "furumapp/postsview.html", context)
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            post_text = form.cleaned_data['text']
            image = form.cleaned_data['image']

            post = Post(
                title=post_title,
                text=post_text,
                user=request.user,
                topic=topic,
                comment_count=0,
                image=image
            )

            post.save()
            post_topic = Topic.objects.get(slug=topic)
            post_topic.increase_count()
        else:
            print('yikes')
        return redirect('posts', topic=topic)

def Post_Details(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post)
        context = {"post": post, "comments": comments}
        return render(request, "furumapp/postdetails.html", context)
    elif request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        post = get_object_or_404(Post, id=post_id)
        comment = Comment(
            text = comment_text,
            timestamp = datetime.datetime.now(),
            user=request.user,
            post=post
        )
        comment.save()
        messages.success(request, 'Comment successful.')
        post.comment_count = post.comment_count + 1
        post.save()
        return redirect('postdetails', post_id=post_id)

def comment_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        comment.delete()
        post.comment_count = post.comment_count - 1
        post.save()

    return redirect('postdetails', post_id)

def post_delete(request, topic, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        post_topic = Topic.objects.get(slug=topic)
        post_topic.decrease_count()

    return redirect('posts', topic=topic)

def search(request):
        if request.method == "GET":
            search_query = request.GET.get('search_query')
            posts = Post.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query))
            comments = Comment.objects.filter(text__icontains=search_query)
            for comment in comments:
                motherpost = Post.objects.filter(id=comment.post.id)
                posts = posts.union(motherpost)
            return render(request, 'furumapp/searchpost.html', {'query': search_query, 'posts': posts})