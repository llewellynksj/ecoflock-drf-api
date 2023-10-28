from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model
    """
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(
        upload_to='images/', default='../EcoFlock/profile_default.png'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.username}'s profile"


# Function using signals to create profile automatically
# from CI DRF-API walkthrough:
def create_profile(sender, instance, created, **kwargs):
    """
    Function to create a profile automatically when a User is created
    """
    if created:
        Profile.objects.create(username=instance)


post_save.connect(create_profile, sender=User)
