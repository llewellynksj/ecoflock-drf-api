from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model
    """
    topic_choices = [
        ('Recycling', 'Recycling'),
        ('Food', 'Food'),
        ('Clothing', 'Clothing'),
        ('Recipes', 'Recipes'),
        ('Energy', 'Energy'),
        ('Products', 'Products'),
        ('Transport', 'Transport'),
    ]
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    topic_category = models.CharField(
        max_length=50,
        choices=topic_choices,
        default='Recycling')
    other_tags = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../EcoFlock/profile_default.png'
    )
    url = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.id}: {self.title} by {self.author}"
