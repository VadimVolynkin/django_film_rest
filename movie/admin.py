from django.contrib import admin

from .models import Category, Actor, Movie, Genre, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'url': ('name',)}

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'url': ('name',)}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'url': ('name',)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'url': ('name',)}

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'pk')

