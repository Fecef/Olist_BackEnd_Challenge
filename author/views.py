# from rest_framework.views import APIView, Response, Request, status
from rest_framework.generics import ListCreateAPIView

from author.serializers import AuthorSerializer
from .models import Author


class AuthorView(ListCreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
