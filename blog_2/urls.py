from django.urls import path
from . import views

app_name = 'blog_2'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]