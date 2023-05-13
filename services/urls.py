from django.conf.urls import url, include
from django.urls import path
from .views import serviceview




urlpatterns = [
    path('',  serviceview, name="serviceview"),
]