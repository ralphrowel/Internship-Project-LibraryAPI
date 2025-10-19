from rest_framework import serializers
from .models import Book, Author
from booktype.serializers import LanguageSerializer, CategorySerializer, GenreSerializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    language = LanguageSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
