from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("catalog:index"))
        else:
            error_context = {
                "error": "Invalid credentials"
            }
        return render(request, "accounts/login.html", context=error_context)


def logout_view(request):
    logout(request)
    return render(request, "accounts/logged_out.html")
