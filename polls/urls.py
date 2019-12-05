from django.urls import path

from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('first', views.first, name='first'),
    path('read', views.read, name='read'),
    path('ques/add', views.add_ques, name='add_ques'),
]
