from django.contrib import admin
from .models import Book, Author, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_year']
    list_filter = ['author', 'categories', 'published_year']
    search_fields = ['title', 'author__name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio']
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
