from django.db import models
from django.conf import settings

# Create your models here.
class Genres(models.Model):
    name = models.CharField(max_length=100)

class Movies(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Reviews(models.Model):
    content = models.CharField(max_length=100)
    score = models.IntegerField()
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

