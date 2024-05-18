from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_count = models.IntegerField()
    topic = models.CharField(max_length=100, default="unspecified")

class Comment(models.Model):
    text = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)









