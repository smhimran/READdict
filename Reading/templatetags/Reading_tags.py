from django import template
import math
import datetime
from ..models import Book, Read

register = template.Library()


@register.filter()
def related(category, book):
    return Book.objects.filter(category=category).exclude(id=book.id)[:1]


@register.filter()
def percent(pages, book):
    total = Book.objects.get(id=book).pages
    ret = (pages/total)*100.
    ret = round(ret, 2)
    return ret


@register.simple_tag()
def recommend(pages, book, user):
    total = Book.objects.get(id=book).pages
    started = Read.objects.filter(book_id=book, user_id=user).exists()
    avg = 0
    if started:
        target = Read.objects.get(book_id=book, user_id=user).target
        days = (target - datetime.date.today()).days
        avg = math.ceil((total-pages)/days)
    return avg
