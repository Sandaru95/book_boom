from django.views import generic
from .models import ContactMessage


class IndexView(generic.CreateView):
    model = ContactMessage
    fields = ['full_name','phone_number','email_address','message']
    template_name = 'contact/index.html'
