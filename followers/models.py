from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    username = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['username', 'followed']

    def __str__(self):
        return f'{self.username} is following {self.followed}'
