from django.contrib import admin
from .models import Book, BookType

admin.site.register(Book)
admin.site.register(BookType)
