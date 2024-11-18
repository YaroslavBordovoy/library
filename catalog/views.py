from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Book, Author, LiteraryFormat


def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_formats = LiteraryFormat.objects.count()
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_formats": num_formats
    }
    return render(request, "catalog/index.html", context=context)


# def literary_format_list_view(request: HttpRequest) -> HttpResponse:
#     literary_format_list = LiteraryFormat.objects.all()
#     context = {
#         "literary_format_list": literary_format_list,
#     }
#     return render(request, "catalog/literary_format_list.html", context=context)


class LiterariFormatListView(generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"


class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")


# def book_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
#     book = Book.objects.get(id=pk)
#     context = {
#         "book": book,
#     }
#     return render(request, "catalog/book_detail.html", context=context)


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author

