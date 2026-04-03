from django.urls import path
from . import views

urlpatterns = [
    path("", views.reports_home, name="reports_home"),
    path("download/", views.download_report_pdf, name="download_report_pdf"),
]
