from django.urls import path

from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('demo/write_csv', views.write_csv, name='write_csv'),
    path('demo/read_csv', views.read_csv, name='read_csv')
]
