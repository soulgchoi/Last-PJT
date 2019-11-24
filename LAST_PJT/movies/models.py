from django.db import models
from django.conf import settings

class Boxoffice(models.Model):
    term_s = models.IntegerField()
    term_e = models.IntegerField()
    rank = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=30)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    poster_url = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class Rating(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)