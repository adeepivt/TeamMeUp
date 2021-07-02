from django.urls import path
from .views import admin_register, admin_login, user_register, user_login

urlpatterns = [
    path('admin-register/', admin_register),
    path('admin-login/', admin_login),
    path('user-register/', user_register),
    path('user-login/', user_login),
]