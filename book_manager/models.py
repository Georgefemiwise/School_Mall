from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    available = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title
    
    

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    
    def __str__(self):
        return f"{self.by} borrowed {self.book}"
	
    
