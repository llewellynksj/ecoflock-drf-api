from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Event(models.Model):
  """
  Event model
  Allows User to create events
  Allows Users to mark an event as 'interested in'
  """
  title = models.CharField(max_length=255)
  date = models.DateField()
  time = models.TimeField()
  description = models.TextField()
  image = models.ImageField(
    upload_to='images/',
    default='../EcoFlock/profile_default.png'
  )
  url = models.URLField
  city = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  cost = models.PositiveIntegerField()
  users_interested = ArrayField(
    ArrayField(
      models.ForeignKey(
        User, on_delete=models.CASCADE)))
  created_by = models.ForeignKey(User, on_delete=CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-date']

  def __str__(self):
    return f"{self.title} - {self.date} - {self.city}"
