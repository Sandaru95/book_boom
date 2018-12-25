from django.views import generic
from .models import Blog_Post
from django.shortcuts import render


class IndexView(generic.ListView):
    model = Blog_Post
    template_name = 'blog/index.html'

class SearchView(generic.View):
    def post(self, request, *kwargs):
        search_term = self.request.POST.get('search_term')
        resultList = Blog_Post.objects.filter(title__contains=str(search_term))
        return render(request, 'blog/result_blog.html', {'result_list':resultList, 'search_term':search_term})
