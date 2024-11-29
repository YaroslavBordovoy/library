
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from .forms import BookForm, AuthorCreationForm, BookSearchForm
from .models import Book, Author, LiteraryFormat


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_formats = LiteraryFormat.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_formats": num_formats,
        "num_visits": num_visits + 1
    }
    return render(request, "catalog/index.html", context=context)


# def literary_format_list_view(request: HttpRequest) -> HttpResponse:
#     literary_format_list = LiteraryFormat.objects.all()
#     context = {
#         "literary_format_list": literary_format_list,
#     }
#     return render(request, "catalog/literary_format_list.html", context=context)


class LiteraryFormatListView(LoginRequiredMixin, generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    queryset = Book.objects.select_related("format")
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = BookSearchForm(
            initial={"title": title}
        )

        return context

    def get_queryset(self):
        title = self.request.GET.get("title")
        if title:
            return self.queryset.filter(title__icontains=title)

        return self.queryset



# def book_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
#     book = Book.objects.get(id=pk)
#     context = {
#         "book": book,
#     }
#     return render(request, "catalog/book_detail.html", context=context)


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author


def test_session_view(request):
    return  HttpResponse(
        "<h1>Test session</h1>"
        f"<h4>Session data: {request.session['book']}</h4>"
    )


def book_create_view(request: HttpRequest) -> HttpResponse:
    # if request.method == "GET":
    #     return render(request, "catalog/book_form.html")
    # elif request.method == "POST":
    #     title = request.POST["title"]
    #     price = request.POST["price"]
    #     Book.objects.create(
    #         title=title,
    #         price=price,
    #         format=LiteraryFormat.objects.get(id=1),
    #         authors=Author.objects.get(id=1)
    #     )
    #     return HttpResponseRedirect(reverse("catalog:book-list"))

    if request.method == "GET":
        context = {
            "form": BookForm()
        }
        return render(request, "catalog/book_form.html", context=context)
    elif request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse("catalog:book-list"))
        else:
            context = {
                "form": form,
            }
            return render(request, "catalog/book_form.html", context=context)


class LiteraryFormatCreateView(LoginRequiredMixin, generic.CreateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = LiteraryFormat
    fields = "__all__"
    success_url = reverse_lazy("catalog:literary-format-list")
    template_name = "catalog/literary_format_form.html"


class LiteraryFormatDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_confirm_delete.html"
    success_url = reverse_lazy("catalog:literary-format-list")


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorCreationForm
    success_url = reverse_lazy("catalog:author-list")


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = "__all__"


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm


# string