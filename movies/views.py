from django.shortcuts import render, redirect, get_object_or_404
from .models import Movies, Genres, Reviews

# Create your views here.

def index(request):
    return render(request, 'movies/index.html')

def detail(request, movie_pk):
    pass

def create_review(request, movie_pk):
    pass

def delete_review(request, movie_pk, review_pk):
    pass

def like(request, movie_pk):
    pass