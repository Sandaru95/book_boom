from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import Blog_Post
from .models import Comment
from django.contrib.auth.models import User


class IndexView(generic.TemplateView):
    template_name = '404.html'


class PostView(generic.DetailView):
    model = Blog_Post
    template_name = 'blog_post/index.html'

class CommentCreateView(generic.View):

    def get(self, request):
        return render(request, '404.html')


    def post(self, request):
        comment_owned_post = Blog_Post.objects.get(pk=request.POST['post_id'])
        comment = Comment(post=comment_owned_post, owner=request.user, comment=self.request.POST['comment'])
        comment.save()
        return HttpResponseRedirect(reverse('blog_post:post_detail', kwargs={'pk': comment_owned_post.pk}))

