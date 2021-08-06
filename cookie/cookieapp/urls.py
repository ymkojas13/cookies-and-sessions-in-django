from django.contrib import admin
from django.urls import path
from cookieapp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('set', views.setcookie, name = 'set'),
    path('del', views.delcookie, name = 'del'),
    path('get', views.getcookie, name = 'get'),
]
