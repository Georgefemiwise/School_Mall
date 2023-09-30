from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name="index"),
    path('all', views.book, name="books"),
    # path('book/add/', views.add_book, name="books"),
    # path('book/<str:id>/delete/', views.delete_book, name="books"),
    # path('book/<str:id>/update/', views.update_book, name="books"),
  
]
