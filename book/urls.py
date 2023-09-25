from django.urls import path

from .views import BookDetailView, BookView


urlpatterns = [
    path("book/", BookView.as_view()),
    path("book/<str:book_id>/", BookDetailView.as_view()),
]
