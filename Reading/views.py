from django.shortcuts import render
from .models import Book, Category

# Create your views here.
def index(request):
    categories = Category.objects.all()[:15]
    return render(request, 'Reading/index.html', {'categories': categories})

def books(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, 'Reading/shop-grid.html', {'books': books, 'categories': categories})

def books_by_category(request,id):
    books = Book.objects.filter(category=id)
    categories = Category.objects.all()
    return render(request, 'Reading/shop-grid.html', {'books': books, 'categories': categories})