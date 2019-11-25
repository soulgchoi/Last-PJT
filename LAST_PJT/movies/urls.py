from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/like/', views.like_movie, name='like_movie'),
    path('<int:movie_id>/rating/', views.create_rating, name='create_rating'),
    path('<int:movie_id>/<int:rating_id>/edit', views.edit_rating, name='edit_rating'),
    path('<int:movie_id>/<int:rating_id>/delete', views.delete_rating, name='delete_rating'),
]
