from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Library API",
        default_version="v1",
        description="""
        * API Usage Notes
        Authentication: Bearer <token> (JWT required for protected routes)
        Base URL: http://127.0.0.1:8000/
        Common status codes: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found
        Content type: application/json
        
        * Dev / Debug Notes
        Run tests with: pytest lib/tests/test_tasks.py
        Reset DB: python manage.py flush && python manage.py migrate
        Create superuser: python manage.py createsuperuser
        Swagger UI at /swagger/
        ReDoc UI at /redoc/
        
        * Keywords for Context
        CRUD = Create, Read, Update, Delete
        JWT = JSON Web Token (for login/authentication)
        DRF = Django Rest Framework
        Pytest = test runner
        """,
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

schema_view.authentication_classes = []

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
}
SWAGGER_SETTINGS = {
    "TAGS_SORTER": "manual",
    "TAGS": [
        {"name": "Users", "description": "Manage users and registration"},
        {"name": "Token", "description": "JWT Authentication (login/refresh)"},
        {"name": "Books", "description": "Manage library books"},
        {"name": "Reviews", "description": "Book reviews"},
    ],
}