import django_filters

from book.models import Book


class BookFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method="filter_name")
    publication_year = django_filters.NumberFilter()
    edition = django_filters.NumberFilter()
    authors = django_filters.CharFilter(method="filter_authors")

    def filter_name(self, queryset, name, value):
        value = value.replace("-", " ")
        return queryset.filter(name__icontains=value)

    def filter_authors(self, queryset, name, value):
        value = value.replace("-", " ")
        return queryset.filter(authors__name__icontains=value)

    class Meta:
        model = Book
        fields = ["name", "publication_year", "edition", "authors"]
