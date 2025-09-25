

ADMIN = 'admin'
LIBRARIAN = 'librarian'
USER = 'user'

ROLE_CHOICES = [
    (ADMIN, 'Admin'),
    (LIBRARIAN, 'Librarian'),
    (USER, 'User'),
]

PERMISSIONS = {
    ADMIN: ['add_book', 'edit_book', 'delete_book', 'search_book'],
    LIBRARIAN: ['add_book', 'edit_book', 'search_book'],
    USER: ['search_book'],
}
