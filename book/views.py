from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .filters import BookFilter
from .models import Book
from .serializers import (
    BookPatchSerializer,
    BookRetrieveSerializer,
    BookSerializer,
)


class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    def perform_create(self, serializer):
        serializer.save(authors=self.request.data["authors"])


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return BookPatchSerializer

        return BookRetrieveSerializer

    lookup_url_kwarg = "book_id"
