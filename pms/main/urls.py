from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('email', views.email, name='email'),
    path('order', views.order, name='order'),
]