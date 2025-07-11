from django.urls import path
from .import views


urlpatterns = [
    path('', views.say_hello, name='home'), 
    path('services/', views.services, name='services'),  # <-- ADD THIS
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('paintTip/', views.tips, name='tips'),
    path('login/', views.login_view, name='login'), # <-- THIS is important
     path('admin/', views.admin_dashboard, name='admin_dashboard'),
]