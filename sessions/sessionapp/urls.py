from django.contrib import admin
from django.urls import path
from sessionapp import views

urlpatterns = [
    path('', views.setsession, name = 'index'),
    path('get', views.getsession, name = 'get'),
    path('del', views.delsession, name = 'del'),
]