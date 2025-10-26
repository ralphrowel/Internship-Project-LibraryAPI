import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'book_type__genre__name': ['exact', 'icontains'],
            'book_type__language__name': ['exact'],
            'publication_date': ['year', 'gte', 'lte'],
        }


# /api/books/?genre=fantasy
# /api/books/?language=english
# /api/books/?publication_date_after=2020-01-01&publication_date_before=2023-12-31
# /api/books/?search=rowling
# /api/books/?ordering=-publication_date