from django.contrib import admin
from .models import Book, Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    search_fields = ('name', 'country')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'language', 'publication_date')
    list_filter = ('language', 'categories', 'genres')
    search_fields = ('title', 'author__name')
    filter_horizontal = ('categories', 'genres')
