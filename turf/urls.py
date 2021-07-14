from django.urls import path
from .views import home_page, add_turf

urlpatterns = [
    path('', home_page, name='home'),
    path('admin-home/', add_turf, name='admin-home'),
]