from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View, TemplateView
from book_1.models import Book


class IndexView(View):
    template_name = 'books/index.html'

    def get(self, request):
        book_list = Book.objects.all()
        book_filtered = []
        book_count = 0
        for book in book_list:
            if book_count >= 6:
                break
            else:
                book_filtered.append(book)
                book_count += 1
        all_book_count = len(book_list)

        return render(request, self.template_name, {'book_list':book_filtered, 'all_book_count':all_book_count})
