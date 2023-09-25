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
    # def get_queryset(self):
    #     queryset = Book.objects.all()

    #     name = self.request.query_params.get("name", None)
    #     authors = self.request.query_params.get("authors", None)
    #     publication_year = self.request.query_params.get("publication_year", None)
    #     edition = self.request.query_params.get("edition", None)

    #     if name:
    #         name = name.replace("-", " ")
    #         queryset = queryset.filter(name__icontains=name)

    #     if authors:
    #         authors = authors.replace("-", " ")
    #         queryset = queryset.filter(authors__name__icontains=authors)

    #     if publication_year:
    #         queryset = queryset.filter(publication_year=publication_year)

    #     if edition:
    #         queryset = queryset.filter(edition=edition)

    #     return queryset

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

        if self.request.method == "GET":
            return BookRetrieveSerializer

    lookup_url_kwarg = "book_id"
