from django.urls import path
from .views import production_home, add_order, update_status

urlpatterns = [
    path('', production_home, name='production_home'),
    path('add/', add_order, name='add_order'),
    path('status/<int:pk>/', update_status, name='update_status'),
]
