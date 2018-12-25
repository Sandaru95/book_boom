from django.db import models
from book_1.models import BookType, Book

class Item(models.Model):
    book_type = models.ForeignKey(BookType, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    qty = models.IntegerField()
    price = models.IntegerField()
    item_total = models.IntegerField()
    book_image_url = models.CharField(max_length=10000)

    def __str__(self):
        return str(self.title) + ' - ' + str(self.qty)
