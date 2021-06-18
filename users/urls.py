from django.urls import path
from .views import user_register

urlpatterns = [
    path('', user_register)
]