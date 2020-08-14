from django.urls import path
from . import views

app_name = 'Reading'

urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.books, name='books'),
    path('books-by-category/<int:id>', views.books_by_category, name='books_by_category'),
]