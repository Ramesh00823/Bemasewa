# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    
    path('service/<int:id>/', views.service_detail, name='service_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('pan/', views.apply_pan, name='apply_pan'),
    path('lifeinsurance/', views.apply_insurance, name='apply_insurance'),
    path('list/pan/', views.list_pan_applications, name='list_pan'),
    path('list/life/', views.list_life_insurance, name='list_life'),

    path('my-pan-status/', views.my_pan_applications, name='my_pan_status'),
    path('my-life-status/', views.my_life_applications, name='my_life_status'),


    # PAN
    path('admin/pan/approve/<int:pk>/', views.approve_pan, name='approve_pan'),
    path('admin/pan/reject/<int:pk>/', views.reject_pan, name='reject_pan'),

    # Life Insurance
    path('admin/life/approve/<int:pk>/', views.approve_life, name='approve_life'),
    path('admin/life/reject/<int:pk>/', views.reject_life, name='reject_life'),


]
