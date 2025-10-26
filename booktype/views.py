from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter  # only if you made filters.py

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter   # link your custom filter

    search_fields = ['title', 'authors__name', 'book_type__category__name']
    ordering_fields = ['title', 'publication_date']


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
