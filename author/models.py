import uuid

from django.db import models


class Author(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)

    books = models.ManyToManyField("book.Book", related_name="authors")

    class Meta:
        ordering = ["name"]

    def __repr__(self) -> str:
        return f"Author Name: {self.name} [{self.pk}]"
