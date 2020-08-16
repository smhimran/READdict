from django.contrib import admin
from .models import Profile, Book, Author, Category, Read
# Register your models here.
admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Read)