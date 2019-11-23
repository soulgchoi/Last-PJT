from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm


User = get_user_model()


@require_GET
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, '', {
        'users': users,
    })


@require_http_methods(['POST', 'GET'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('')
    else:
        form = CustomUserCreationForm()
    return render(request, '', {
        'form': form,
    })


@require_http_methods(['POST', 'GET'])
def login(requset):
    if requset.user.is_authenticated:
        return redirect('')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('')
    else:
        form = CustomAuthenticationForm()
    return render(request, '', {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('')


@login_required
def follow(request, user_id):
    follower = request.user
    following = get_object_or_404(User, id=user_id)
    if follower != following:
        if following.followers.filter(id=follower.id).exists():
            following.followers.remove(follower)
        else:
            following.followers.add(follower)
    return redirect('', user_id)


@require_GET
@login_required
def user_detail(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    return render(request, '', {
        'user_info': user_info,
    })
