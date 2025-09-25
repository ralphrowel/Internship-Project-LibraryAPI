from rest_framework import viewsets, permissions
from .models import Review
from .serializers import ReviewSerializer
from permissions.custom_permissions import IsOwnerOrReadOnly

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
