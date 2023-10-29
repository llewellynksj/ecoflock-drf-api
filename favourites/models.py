from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Favourite(models.Model):
    """

    """
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='favourites', on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['username', 'post']

    def __str__(self):
        return f"{self.username} - {self.post}"
