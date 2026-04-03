from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard_home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', dashboard_home, name='dashboard'),

    path('inventory/', include('inventory.urls')),
    path('reports/', include('reports.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
