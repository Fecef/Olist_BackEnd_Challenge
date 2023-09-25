from rest_framework.generics import ListCreateAPIView

from .models import Author
from .serializers import AuthorCreateSerializer, AuthorListSerializer


class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AuthorListSerializer

        if self.request.method == "POST":
            return AuthorCreateSerializer

    def perform_create(self, serializer):
        serializer.save(books=[])
