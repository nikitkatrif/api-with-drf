from django.contrib import admin
from .models import Platform, Genre, Game

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'platform', 'release_year', 'rating')
    list_filter = ('platform', 'genres', 'release_year')
    search_fields = ('title', 'description')