from django.views import generic
from django.shortcuts import render
from book_1.models import Book, BookType


class IndexView(generic.View):
    queryset = Book
    template_name = 'book_4/index.html'

    def get(self, request):
        advice_type = BookType.objects.get(pk=4)
        list_of_advice = advice_type.book_set.all()

        return render(request, self.template_name, {'object_list':list_of_advice})
