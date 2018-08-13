from django.urls import path
from . import views

app_name = 'book_4'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]