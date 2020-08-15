from django import template

register = template.Library()

from ..models import Book

@register.filter()
def related(category, book):
    return Book.objects.filter(category=category).exclude(id=book.id)[:1]