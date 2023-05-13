from django.conf.urls import url, include
from django.urls import path
from .views import contactview, all_contacts


app_name = "contact"

urlpatterns = [
    path('',  contactview, name="contactview"),
    path("list/", view=all_contacts, name="contactlist"),

]