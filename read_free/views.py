from django.shortcuts import render
from django.views import generic
from book_1.models import Book, BookType

class IndexView(generic.ListView):
    queryset = Book.objects.filter(read_free=True)
    template_name = 'read_free/index.html'