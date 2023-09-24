from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Author
        fields = ["name"]
