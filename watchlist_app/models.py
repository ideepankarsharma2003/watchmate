from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(default='', null=True, blank=True)
    active= models.BooleanField(default=True)
    genre = models.CharField(max_length=100, default='', null=True, blank=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title