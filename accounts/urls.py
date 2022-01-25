from django.urls import path

from . import views

urlpatterns = [
    path('login', views.loginhere, name='login'), 
    path('register', views.register, name='register'), 
    path('logout', views.logouthere, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),    
]
