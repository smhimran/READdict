from django.urls import path
from . import views

app_name = 'Reading'

urlpatterns = [

    path('books/', views.books, name='books'),
    path('books-by-category/<int:id>', views.books_by_category, name='books_by_category'),
    path('check-user/', views.check_user, name='check-user'),
    path('start_reading/', views.start_reading, name='start_reading'),
    path('increse_page_count/', views.increase_page_count, name='increase_page_count'),
    path('book/<int:id>', views.single_book, name='single_book'),
]