from django.urls import path
from . import views

app_name = 'read_free'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]