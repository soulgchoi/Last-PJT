from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http.response import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
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
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                user = User.objects.create(
                    username=form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                user.last_name = form.cleaned_data['last_name']
                user.first_name = form.cleaned_data['first_name']
                user.set_password(user.password)
                user.save()
                auth_login(request, user)
                return redirect('accounts:user_list')   
            else:
                return render(request, 'accounts/signup.html', {
                    'form': form
                })
    else:
        form = CustomUserCreationForm()

    messages = form.errors
    return render(request, 'accounts/signup.html', {
        'form': form,
        'messages': messages,
    })


@require_http_methods(['POST', 'GET'])
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:user_list')

    if request.method == "POST":
        form = CustomAuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user: 
            auth_login(request, user) 
            return redirect('accounts:user_list')
        else:
            return render(request, 'accounts/login.html', {
            'form': form,
        })
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
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
