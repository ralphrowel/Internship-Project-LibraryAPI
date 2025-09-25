from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from permissions.custom_permissions import IsLibrarian, IsAdmin

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsLibrarian]
        elif self.action == 'destroy':
            permission_classes = [IsAdmin]
        elif self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
