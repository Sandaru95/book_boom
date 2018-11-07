from django.db import models
from django.shortcuts import reverse


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email_address = models.EmailField(max_length=255)
    message = models.TextField(max_length=5000)

    def __str__(self):
        return str(self.full_name)

    def get_absolute_url(self):
        return reverse('contact:index')

