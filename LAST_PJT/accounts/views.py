from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from datetime import datetime


User = get_user_model()


@require_GET
# @login_required
def user_list(request):
    if not request.user.is_authenticated:
        return redirect('movies:main')

    users = User.objects.all()
    # users = User.objects.all().order_by('follower'.count)
    return render(request, 'accounts/user_list.html', {
        'users': users,
    })


@require_http_methods(['POST', 'GET'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:user_list')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/_form.html', {
        'form': form,
    })


@require_http_methods(['POST', 'GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:user_list')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'accounts:user_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form': form,
    })

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


@login_required
def follow(request, user_id):
    follower = request.user
    following = get_object_or_404(User, id=user_id)
    if follower != following:
        if following.follower.filter(id=follower.id).exists():
            following.follower.remove(follower)
        else:
            following.follower.add(follower)
    return redirect('accounts:user_detail', user_id)


@require_GET
@login_required
def user_detail(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/user_detail.html', {
        'user_info': user_info,
    })
