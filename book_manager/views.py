from django.shortcuts import render, redirect
from .forms import BookForms
from .models import Book


def index(request):
    return render(request, "index.html")

def sayHi(request):
    form = BookForms()
    context={"form":form}
    return render(request, "books/home.html", context)


def book(request):
    all_books = Book.objects.all()
    context ={"books" : all_books}
    return render(request, "books/books.html", context)

