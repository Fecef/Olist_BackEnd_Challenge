import uuid

from django.db import models


class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    edition = models.PositiveSmallIntegerField()
    publication_year = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["name"]

    def __repr__(self) -> str:
        return f"Book Name: {self.name} [{self.pk}]"
