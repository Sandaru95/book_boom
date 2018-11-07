from django.urls import path
from . import views

app_name = 'blog_post'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.PostView.as_view(), name='post_detail'),
    path('create-comment/', views.CommentCreateView.as_view(), name='create_comment'),
]