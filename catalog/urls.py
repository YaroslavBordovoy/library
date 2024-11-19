from django.urls import path

from catalog.views import index, LiteraryFormatListView, BookListView, AuthorListView, BookDetailView, test_session_view

urlpatterns = [
    path("", index, name="index"),
    # path("literary-formats/", literary_format_list_view, name="literary-format-list"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("books/", BookListView.as_view(), name="book-list"),
    # path("books/<int:pk>/", book_detail_view, name="book-detail"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("test-session/", test_session_view, name="test-session"),
]

app_name = "catalog"
