from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'blog_1/index.html'
