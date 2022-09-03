from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def index(request):
    return render(request, "auctions/index.html", {})


def login_view(request):
    return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    return render(request, "auctions/register.html")
