from django.views import generic
from django.http import HttpResponse

class IndexView(generic.TemplateView):
    template_name = 'services/index.html'
