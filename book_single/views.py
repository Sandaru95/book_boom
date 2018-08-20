from django.views import generic
from book_1.models import Book, BookType
from django.shortcuts import get_object_or_404


class IndexBookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_single/index_book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_books = []
        book_count = 0

        book_type_1 = BookType.objects.get(pk=1)
        book_type_2 = BookType.objects.get(pk=2)
        book_type_3 = BookType.objects.get(pk=3)
        book_type_4 = BookType.objects.get(pk=4)

        current_book = get_object_or_404(Book, pk=self.kwargs['pk'])

        if current_book.book_type.title == book_type_1.title:
            for book in book_type_1.book_set.all():
                if book_count >= 4:
                    break
                else:
                    related_books.append(book)
                    book_count += 1
            context['related_book_list'] = related_books
        if current_book.book_type.title == book_type_2.title:
            for book in book_type_2.book_set.all():
                if book_count >= 4:
                    break
                else:
                    related_books.append(book)
                    book_count += 1
            context['related_book_list'] = related_books
        if current_book.book_type.title == book_type_3.title:
            for book in book_type_3.book_set.all():
                if book_count >= 4:
                    break
                else:
                    related_books.append(book)
                    book_count += 1
                    context['related_book_list'] = related_books
        if current_book.book_type.title == book_type_4.title:
            for book in book_type_4.book_set.all():
                if book_count >= 4:
                    break
                else:
                    related_books.append(book)
                    book_count += 1
            context['related_book_list'] = related_books

        return context
