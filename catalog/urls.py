from django.urls import path

from catalog.views import index, LiterariFormatListView, BookListView, AuthorListView, BookDetailView

urlpatterns = [
    path("", index, name="index"),
    # path("literary-formats/", literary_format_list_view, name="literary-format-list"),
    path("literary-formats/", LiterariFormatListView.as_view(), name="literary-format-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    # path("books/<int:pk>/", book_detail_view, name="book-detail"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
]

app_name = "catalog"
