from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from datetime import datetime
import random

from .models import Movie, Genre, Boxoffice, Rating
from .forms import RatingModelForm


def main(request):
    return render(request, 'movies/mainpage.html')

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
    # if not request.user.is_authenticated:
    #     return redirect('movies:main')

    # 박스오피스 순위
    boxoffices = Boxoffice.objects.all()
    now = datetime.now()
    date = str(now.month) + str(now.day)
    year = str(now.year)
    y1_term, y5_term, y10_term = '', '', ''
    for boxoffice in boxoffices:
        term_s = int(boxoffice.term[4:8])
        term_e = int(boxoffice.term[13:])
        term_y = int(boxoffice.term[:4])
        if term_s <= int(date) <= term_e:
            if int(year) - 1 == term_y:
                y1_term = boxoffice.term
            elif int(year) - 5 == term_y:
                y5_term = boxoffice.term
            elif int(year) - 10 == term_y:
                y10_term = boxoffice.term
    y1_movies = Boxoffice.objects.filter(term=y1_term)[:5]
    y5_movies = Boxoffice.objects.filter(term=y5_term)[:5]
    y10_movies = Boxoffice.objects.filter(term=y10_term)[:5]

    # 랜덤 출력
    num_entities = Movie.objects.all().count()
    rand_entities = random.sample(range(num_entities), 5)
    ran_movies = Movie.objects.filter(id__in=rand_entities)

    # 추천 알고리즘
    user = request.user  # 유저가
    recommend_movies = ''
    rcmmd_movies = []
    # if user.like_movies.all().exists():  # 좋아하는 영화가 있으면
    #     user_likes = user.like_movies.all()  # 그 영화들
    #     for like in user_likes:
    #         if like.like_users.all().exists():  # 을 좋아하는 다른 유저들
    #             like_users = like.like_users.all()
    #             for likeuser in like_users:  # 이 좋아하는 다른 영화
    #                 rcmmd_movies += likeuser.like_movies.all()
    #     res = ''
    ids = []
    for rcmmd in rcmmd_movies:
        ids += [rcmmd.id]
    # if len(ids) < 20:
    #     ids += random.sample(range(num_entities), 20-len(ids))
    res = Movie.objects.filter(id__in=ids[:11])

    return render(request, 'movies/movie_list.html', {
        'y1_movies': y1_movies,
        'y5_movies': y5_movies,
        'y10_movies': y10_movies,
        'ran_movies': ran_movies,
        'rcmmd_movies': res,
    })

    

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
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    if movie.like_users.filter(id=user.id).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    return redirect('movies:movie_detail', movie_id)
