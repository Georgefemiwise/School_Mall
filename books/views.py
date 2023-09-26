from django.shortcuts import render
from .forms import BookForms


def index(request):

    return render(request, "index.html")

def sayHi(request):
    form = BookForms()
    context={"form":form}
    return render(request, "books/home.html", context)


def book(request):
    if request.method == "POST":
        print('hello')
    return render(request, "books/books.html", )

def add_book(request):
    if request.method == "POST":
        print('hello')
    return render(request, "books/books.html", )

def delete_book(request,id):
    if request.method == "POST":
        print('hello')
    return render(request, "books/books.html", )

def update_book(request, id):
    if request.method == "POST":
        print('hello')
    return render(request, "books/books.html", )
