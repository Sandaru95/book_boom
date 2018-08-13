from django.views import generic
from django.shortcuts import render
from book_1.models import Book, BookType


class IndexView(generic.View):
    queryset = Book
    template_name = 'book_3/index.html'

    def get(self, request):
        children_type = BookType.objects.get(pk=3)
        list_of_children = children_type.book_set.all()

        return render(request, self.template_name, {'object_list':list_of_children})
