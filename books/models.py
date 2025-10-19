from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category, related_name='genres', on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='books')
    category = models.ForeignKey(Category, related_name='books', on_delete=models.SET_NULL, null=True)
    published_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"


class BookDetail(models.Model):
    book = models.OneToOneField(Book, related_name='details', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=100)
    page_count = models.IntegerField()
    language = models.CharField(max_length=30, default='English')

    def __str__(self):
        return f"Details of {self.book.title}"


class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review on {self.book.title}"
