from django.urls import path
from . import views

urlpatterns = [
    path('', views.application_create, name='application_create'),
    path('dashboard/application/<int:pk>/pdf/', views.application_pdf, name='application_pdf'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/applications/', views.admin_applications, name='admin_applications'),
    path('dashboard/application/<int:pk>/', views.admin_application_detail, name='admin_application_detail'),
    path('dashboard/admins/', views.admin_admins, name='admin_admins'),
    path('dashboard/admins/add/', views.admin_add, name='admin_add'),
    path('dashboard/admins/<int:admin_id>/edit/', views.admin_edit, name='admin_edit'),
    path('dashboard/admins/<int:admin_id>/delete/', views.admin_delete, name='admin_delete'),
    path('ajax/load-tumanlar/', views.load_tumanlar, name='ajax_load_tumanlar'),
] 