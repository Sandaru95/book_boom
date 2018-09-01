from django.urls import path
from . import views

app_name = 'book_single'

urlpatterns = [
    path('<int:pk>', views.IndexBookDetailView.as_view(), name='index'),
]