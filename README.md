# Project_07

## 목표 

- 협업을 통한 데이터베이스 모델링 및 기능 구현
- 다양한 형태의 데이터베이스 관계 설정

## App

- `movies`

  - `models.py`

  - ```python
    from django.db import models
    from django.conf import settings
    
    # Create your models here.
    class Genre(models.Model):
        name = models.CharField(max_length=100)
    
    class Movie(models.Model):
        title = models.CharField(max_length=200)
        audience = models.IntegerField()
        poster_url = models.TextField()
        description = models.TextField()
        genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
        like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    
    class Review(models.Model):
        content = models.CharField(max_length=100)
        score = models.IntegerField()
        movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ```

  - `forms.py`

  - ```python
    from django import forms
    from django.db import models
    from . models import Review
    
    
    class ReviewForm(forms.ModelForm):
        class Meta:
            model = Review
            fields =('content','score',)
    ```

- `accounts`

  - `models.py`

  - ```python
    from django.contrib.auth.models import AbstractUser
    from django.conf import settings
    
    class User(AbstractUser):
        follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    ```

  - `forms.py`

  - ```python
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm
    
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = get_user_model()
            fields = ('username','email','first_name','last_name',)
    ```



## Seed Data 반영

- `movies/fixtures`
  - `genre.json`
    - `$ python manage.py loaddata movies/fixtures/genre.json`
  - `movie.json`
    - `$ python manage.py loaddata movies/fixtures/movie.json`
    - `'':'0'`: 오류 데이터 제거

## Design

- `Bootstrap4` 적용
- `Navbar`  `base.html`적용
- `Card` `index.html`,`detail.html` 적용
- `detail.html` `badge`,`button` 적용