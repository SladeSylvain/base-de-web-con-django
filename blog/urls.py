from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
    path('posts/', views.posts, name='posts'),
    path('gatitos/',views.gatitos, name='gatitos')
]