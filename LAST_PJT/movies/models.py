from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=30)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Boxoffice(models.Model):
    term = models.IntegerField()
    rank = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Rating(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)