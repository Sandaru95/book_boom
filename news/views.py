from django.views import generic
from .models import News


class IndexView(generic.ListView):
    model = News
    template_name = 'news/index.html'
