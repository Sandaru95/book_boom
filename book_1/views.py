from django.views import generic
from django.shortcuts import render
from .models import Book, BookType


class IndexView(generic.View):
    queryset = Book
    template_name = 'book_1/index.html'

    def get(self, request):
        novel_type = BookType.objects.get(pk=1)
        list_of_novel = novel_type.book_set.all()

        return render(request, self.template_name, {'object_list':list_of_novel})