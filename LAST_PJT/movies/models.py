from django.db import models
from django.conf import settings
import csv
from datetime import datetime

class Genre(models.Model):
    name = models.CharField(max_length=30)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    opendate = models.DateField()
    audience = models.IntegerField()
    poster_url = models.TextField()
    description_head = models.TextField()
    description = models.TextField()
    codes = models.CharField(max_length=10)
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


    @classmethod
    def import_movie(cls):
        with open('./movies/fixtures/movies_import.csv', 'r', encoding='utf-8') as f:
            movies = csv.DictReader(f)
            for movie in movies:
                genres_in_movie = list(movie['genres'].split(','))
                m = cls.objects.create(                    
                    title = movie['movieNm'],
                    opendate = datetime.strptime(movie['openDt'], '%Y-%m-%d'),
                    audience = int(movie['audiAcc']),
                    poster_url = movie['poster_url'],
                    description_head = movie['head'],
                    description = movie['description'],
                    codes = movie['movieCd']
                )
                for genre in genres_in_movie:
                    g = Genre.objects.get(name=genre)
                    m.genres.add(g)


class Boxoffice(models.Model):
    term = models.CharField(max_length=17)
    rank = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    @classmethod
    def import_boxoffice(cls):
        with open('./movies/fixtures/movie_id.csv', 'r', encoding='utf-8') as f:
            movies = csv.DictReader(f)
            for mv in movies:
                m = cls.objects.create(
                    term = mv['showRange'],
                    rank = mv['rank'],
                    movie = Movie.objects.get(codes=mv['movieCd'])
                )


class Rating(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    