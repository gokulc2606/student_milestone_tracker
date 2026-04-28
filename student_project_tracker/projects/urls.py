from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_project, name='register_project'),
    path('upload/<int:project_id>/', views.upload_milestone, name='upload_milestone'),
    path('dashboard/', views.guide_dashboard, name='dashboard'),
    path('export/', views.export_csv, name='export_csv'),
    path('api/check-title/', views.api_check_title, name='api_check_title'),
]
