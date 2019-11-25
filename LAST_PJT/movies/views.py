from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from datetime import datetime

from .models import Movie, Genre, Boxoffice, Rating
from .forms import RatingModelForm
# Create your views here.


# movie detail
# movie_list > 날짜별 박스오피스
# movie_list2 > 추천 알고리즘

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    rating_form = RatingModelForm()
    is_like = movie.like_users.filter(id=request.user.id).exists()
    genres = movie.genres.all()
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'rating_form': rating_form,
        'is_like': is_like,
        'genres': genres,
    })


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {
        'movies': movies,
    })

# def movie_list(request):
#     # 박스오피스 순위
#     now = datetime.now()
#     # 추천 알고리즘
#     pass


# def recommendation():
    



@login_required
@require_POST
def create_rating(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    form = RatingModelForm(request.POST)
    if form.is_valid():
        rating = form.save(commit=False)
        rating.movie = movie
        rating.user = request.user
        rating.save()
    return redirect('movies:movie_detail', movie_id)


@login_required
@require_http_methods(['GET', 'POST'])
def edit_rating(request, movie_id, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    if request.method == 'POST':
        form = RatingModelForm(request.POST, instance=rating)
        if form.is_valid():
            rating = form.save()
            return redirect('movies:movie_detail', movie_id)
    else:
        form = RatingModelForm(instance=rating)

    return render(request, 'movies/movie_detail.html', {
        'form': form,
    })


@login_required
@require_POST
def delete_rating(request, movie_id, rating_id):
    movie = get_object_or_404(Movie, id=movie_id)
    rating = get_object_or_404(Rating, id=rating_id)
    if rating.user == request.user:
        rating.delete()
    return redirect('movies:movie_detail', movie_id)


@login_required
def like_movie(request, movie_id):
    movie - get_object_or_404(Movie, id=movie_id)
    user = request.user
    if movie.like_users.filter(id=user.id).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    return redirect('movies:movie_detail', movie_id)
