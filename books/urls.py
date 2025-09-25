from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
