from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "edition", "publication_year", "authors"]


class BookRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "edition", "publication_year", "authors"]
        depth = 1


class BookPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "name", "edition", "publication_year"]
