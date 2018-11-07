from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('register-failed/', views.RegisterFailedView.as_view(), name='register_failed'),
    path('register-success/', views.RegisterSuccessView.as_view(), name='register_success'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]