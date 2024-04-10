from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")
    published_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments")
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'
