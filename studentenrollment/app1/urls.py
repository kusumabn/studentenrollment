from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('ajax/register/', views.ajax_register_student, name='ajax_register'),
    path('export/csv/', views.export_students_csv, name='export_csv'),
    path('export/pdf/', views.export_students_pdf, name='export_pdf'),
]