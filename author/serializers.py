from rest_framework import serializers

from author.models import Author


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "books"]
        read_only_fields = ["books"]


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]
