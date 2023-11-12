from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from threads.models import Thread


class UpVote(models.Model):
  """
  UpVote model
  Allowers User to up-vote a post or thread
  """
  username = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(
    Post,
    on_delete=models.CASCADE,
    blank=True)
  thread = models.ForeignKey(
    Thread,
    on_delete=models.CASCADE,
    blank=True)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f"Up-vote by {self.username}"


class DownVote(models.Model):
  """
  DownVote model
  Allowers User to down-vote a post or thread
  """
  username = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(
    Post,
    on_delete=models.CASCADE,
    blank=True)
  thread = models.ForeignKey(
    Thread,
    on_delete=models.CASCADE,
    blank=True)
  created_on = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created_on']
  
  def __str__(self):
    return f"Down-vote by {self.username}"
