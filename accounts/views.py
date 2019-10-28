from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    persons = get_user_model().objects.all()
    context = {
        'persons':persons,
    }
    return render(request, 'accounts/index.html', context)


def create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')

    form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)

def detail(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    reviews = person.review_set.all()
    movies = person.like_movies.all()
    context = {
        'person': person,
        'reviews':reviews,
        'movies':movies,
    }
    return render(request, 'accounts/detail.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/auth_form.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')
    
@login_required
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(),pk=user_pk)
    user = request.user
    if person.follower.filter(pk=user.pk).exists():
        person.follower.remove(user)
    else:
        person.follower.add(user)
    return redirect('accounts:detail', user_pk)