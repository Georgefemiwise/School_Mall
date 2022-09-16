from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'products\index.html')


def blog(request):
    return render(request, 'products/blog.html')
