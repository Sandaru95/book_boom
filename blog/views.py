from django.views import generic
from .models import Blog_Post


class IndexView(generic.ListView):
    model = Blog_Post
    template_name = 'blog/index.html'
