from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('add/', views.add_material, name='add_material'),
    path('edit/<int:pk>/', views.edit_material, name='edit_material'),
    path('delete/<int:pk>/', views.delete_material, name='delete_material'),
    path('low-stock/', views.low_stock, name='low_stock'),
]
