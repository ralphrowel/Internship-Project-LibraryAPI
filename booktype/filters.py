from django_filters import rest_framework as filters
from .models import Book


class BookFilter(filters.FilterSet):
    # Filter books published between two dates
    publication_date = filters.DateFromToRangeFilter()
    # Partial (case-insensitive) matches
    genre = filters.CharFilter(field_name='book_type__genre__name', lookup_expr='icontains')
    language = filters.CharFilter(field_name='book_type__language__name', lookup_expr='icontains')
    category = filters.CharFilter(field_name='book_type__category__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['genre', 'language', 'category', 'publication_date']

# /api/books/?genre=fantasy
# /api/books/?language=english
# /api/books/?publication_date_after=2020-01-01&publication_date_before=2023-12-31
# /api/books/?search=rowling
# /api/books/?ordering=-publication_date