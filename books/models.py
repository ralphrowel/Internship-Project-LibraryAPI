from django.db import models
from booktype.models import Language, Category, Genre


class Author(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.title
