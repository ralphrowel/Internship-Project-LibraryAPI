from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .swagger import schema_view

urlpatterns = [
    path("admin/", admin.site.urls),

    # JWT Authentication
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # App endpoints
    path("api/users/", include("users.urls")),
    path("api/books/", include("books.urls")),
    path("api/reviews/", include("reviews.urls")),

    # Swagger
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
