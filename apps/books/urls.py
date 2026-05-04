from django.urls import path
from . import views

urlpatterns = [
    path('', views.buku_list, name='buku_list'),
    path('create/', views.buku_create, name='buku_create'),
    path('<int:pk>/update/', views.buku_update, name='buku_update'),
    path('<int:pk>/delete/', views.buku_delete, name='buku_delete'),
]