from django.contrib import admin
from .models import Book, Borrows
# Register your models here.
admin.site.register(Book)
admin.site.register(Borrows)
