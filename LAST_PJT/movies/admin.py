from django.contrib import admin
from .models import Boxoffice, Genre, Movie, Rating

admin.site.register(Boxoffice)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Rating)
