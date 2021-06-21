from django.urls import path
from .views import admin_register, admin_login

urlpatterns = [
    path('', admin_register),
    path('login/', admin_login)
]