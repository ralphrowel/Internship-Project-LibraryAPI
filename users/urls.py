from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="user-register"),
    path("", views.UserListCreateView.as_view(), name="user-list"),
    path("<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
]
