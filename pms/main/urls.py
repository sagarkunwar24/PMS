from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('email', views.email, name='email'),
=======
    path('order', views.order, name='order'),
>>>>>>> 0dedbba3c12800889b6b66b4c12e615fa7c1c823
]