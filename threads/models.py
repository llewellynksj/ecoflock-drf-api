from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Thread(models.Model):
    """
    Thread model
    Allowers User to comment on a Post
    """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment by {self.username} on {self.created_on}"
