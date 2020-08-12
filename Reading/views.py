from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Reading/index.html')

def books(request):
    return render(request, 'Reading/shop-grid.html')