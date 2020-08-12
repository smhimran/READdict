from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'Reading/index.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'Reading/shop-grid.html', {'books': books})