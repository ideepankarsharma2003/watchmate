from django.db import models



# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    website = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(default='', null=True, blank=True)
    active= models.BooleanField(default=True)
    genre= models.CharField(max_length=100, default='', null=True, blank=True)
    platform= models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist', null=True)
    year= models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title