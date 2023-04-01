from django.db import models
from django.utils import timezone

# Crearemos los modelos de los Blogs.

class Blog (models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='images/', null=True, blank=True, default=None)

    def __str__(self):
        return f'Author: {self.author}, Title: {self.title}, Subtitle: {self.subtitle}'

    class Meta:
        db_table = 'Principal_blog'

