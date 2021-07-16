from django.urls import path
from .views import admin_register, admin_login, admin_home, user_register, user_login

urlpatterns = [
    path('admin-register/', admin_register),
    path('admin-login/', admin_login, name='admin_login'),
    path('admin-home/', admin_home, name='admin_home'),
    path('user-register/', user_register),
    path('user-login/', user_login, name='user_login'),
    
]