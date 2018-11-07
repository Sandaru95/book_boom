from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ListView.as_view(), name='shop_list'),
    path('buy/<int:pk>/', views.BookBuyView.as_view(), name='book_buy'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:pk>/', views.CartRemoveView.as_view(), name='cart_remove'),
]