from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from book_1.models import Book, BookType
from .models import Item

class IndexView(generic.TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        novel = BookType.objects.get(pk=1)
        motivational =  BookType.objects.get(pk=2)
        children = BookType.objects.get(pk=3)
        advice = BookType.objects.get(pk=4)
        context['novel_list'] = novel.book_set.all()[:5]
        context['novel_id'] = novel.pk
        context['motivational_list'] = motivational.book_set.all()[:5]
        context['motivational_id'] = motivational.pk
        context['children_list'] = children.book_set.all()[:5]
        context['children_id'] = children.pk
        context['advice_list'] = advice.book_set.all()[:5]
        context['advice_id'] = advice.pk
        return context

class ListView(generic.View):
    def get(self, request, **kwargs):
        book_type = BookType.objects.get(pk=self.kwargs['pk'])
        books_of_type = book_type.book_set.all()
        return render(request, 'shop/shop_list.html', {'book_list':books_of_type, 'book_type':book_type, 'book_type_pk':book_type.pk})

class BookBuyView(generic.DetailView):
    model = Book
    template_name = 'shop/book_buy.html'

class CartView(generic.ListView):
    model = Item
    template_name = 'shop/cart_index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        sum = 0
        Item.objects.all()
        for object in Item.objects.all():
            sum += (int(object.price) * int(object.qty))
        context['cart_subtotal'] = sum
        context['shipping_price'] = 200
        context['cart_total'] = (int(sum) + 200)
        return context

class CartAddView(generic.View):

    def post(self,request, **kwargs):
        no_item = self.request.POST.get('qty')
        book = Book.objects.get(pk=self.kwargs['pk'])
        book_title = book.title
        book_type = book.book_type
        book_price = book.price
        book_item_total = int(no_item) * int(book_price)
        book_image_url = book.cover_photo.url
        it1 = Item(book_type=book_type, title=book_title, qty=no_item, price=book_price, book_image_url=book_image_url, item_total=book_item_total)
        it1.save()
        return redirect('shop:book_buy', pk=self.kwargs['pk'])

class CartRemoveView(generic.View):

    def post(self, request, **kwargs):
        item_to_delete = Item.objects.get(pk=self.kwargs['pk'])
        item_to_delete.delete()
        return redirect('shop:cart')