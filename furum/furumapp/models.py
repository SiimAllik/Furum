from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_count = models.IntegerField()
    topic = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        if self.image:
            self.image.storage.delete(self.image.name)
        super().delete()

class Comment(models.Model):
    text = models.CharField(max_length=500)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Topic(models.Model):
    topic = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000)
    post_count = models.IntegerField()

    def increase_count(self):
        self.post_count += 1
        self.save()

    def decrease_count(self):
        self.post_count -= 1
        self.save()






