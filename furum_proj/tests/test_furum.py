import django.db.utils
from django.test import TestCase
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from furumapp.models import Post, Comment, Topic
from django.shortcuts import get_object_or_404

class UserManagementTestCase(TestCase):

    def test_user_registration(self):
        User.objects.create_user(username="testuser", password="safepassword1")
        user = get_object_or_404(User, username="testuser")
        self.assertEqual(user.username, "testuser")

class PostingTestCase(TestCase):

    def setUpUser(self):
        User.objects.create_user(username="testuser", password="safepassword1")

    def createTopic(self):
        Topic.objects.create(topic="SONIC", slug="sonic", post_count=0)

    def addPostToSonic(self):
        self.setUpUser()
        user = get_object_or_404(User, username="testuser")
        self.createTopic()
        Post.objects.create(title="Nice long title", text="Great text", user=user, topic="sonic")

    def test_adding_post(self):
        self.addPostToSonic()
        first_post = get_object_or_404(Post, title="Nice long title")
        self.assertEqual(first_post.text, "Great text")

    def test_topic_post_count_increase(self):
        self.createTopic()
        topic = get_object_or_404(Topic, topic="SONIC")
        count = topic.post_count
        topic.increase_count()
        count2 = topic.post_count

        self.assertEqual(count2, count+1)

class CommentingTestCase(TestCase):

    def setUpUser(self):
        User.objects.create_user(username="testuser", password="safepassword1")

    def addPost(self):
        self.setUpUser()
        user = get_object_or_404(User, username="testuser")
        Post.objects.create(title="Nice long title", text="Great text", user=user, topic="")

    def test_adding_comment(self):
        self.addPost()
        first_post = get_object_or_404(Post, title="Nice long title")
        user = get_object_or_404(User, username="testuser")
        Comment.objects.create(text="I like this", user=user, post=first_post)
        comment = get_object_or_404(Comment, text="I like this")
        self.assertEqual(comment.post, first_post)

if __name__ == '__main__':
    main()
