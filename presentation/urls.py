from django.conf.urls import url, include
from django.urls import path
from .views import presentationview




urlpatterns = [
    path('',  presentationview, name="presentationview"),
]