from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter  # ✅ import your custom filters


class BookViewSet(viewsets.ModelViewSet):
    """
    Enhanced Book API View:
    - Uses external filters.py for cleaner structure
    - Supports advanced search, ordering, and filtering
    """
    queryset = Book.objects.select_related('book_type').prefetch_related('authors').all()
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter  # ✅ plug in the custom filter

    search_fields = [
        'title',
        'authors__name',
        'book_type__category__name',
        'book_type__genre__name',
        'book_type__language__name'
    ]
    ordering_fields = ['title', 'publication_date', 'book_type__genre__name']
    ordering = ['title']  # default order

# Filtering:
# /api/books/?book_type__genre__name=Fantasy
# /api/books/?book_type__language__name=English
# /api/books/?publication_date__year=2023

# Searching:
# /api/books/?search=Rowling
# /api/books/?search=Harry

# Ordering:
# /api/books/?ordering=publication_date
# /api/books/?ordering=-title
