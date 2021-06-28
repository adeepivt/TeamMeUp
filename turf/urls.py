from django.urls import path
from .views import add_turf

urlpatterns = [
    path('', add_turf),
]