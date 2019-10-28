from django.contrib import admin
from .models import Movie, Genre

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'audience', 'description', 'genre_id',)
    list_display_links = ('title',)

class GenresAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('name',)

admin.site.register(Movie, MoviesAdmin)
admin.site.register(Genre, GenresAdmin)