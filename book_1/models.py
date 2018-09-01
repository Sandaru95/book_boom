from django.db import models


class BookType(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return str(self.title)


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    book_type = models.ForeignKey(BookType, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    cover_photo = models.FileField()
    preview = models.FileField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.title) + ' - ' + str(self.author)
