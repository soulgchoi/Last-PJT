from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.main, name='main'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_id>/like/', views.like_movie, name='like_movie'),
    path('movies/<int:movie_id>/rating/', views.create_rating, name='create_rating'),
    # path('movies/<int:movie_id>/<int:rating_id>/edit', views.edit_rating, name='edit_rating'),
    path('movies/<int:movie_id>/<int:rating_id>/delete', views.delete_rating, name='delete_rating'),
]
