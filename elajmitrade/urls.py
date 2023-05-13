"""elajmitrade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from home.views import home
from contact.views import contactview, all_contacts
from contact import urls as urls_contact
from django.urls import path, include
from product import urls as urls_product
from product.views import all_products, product_filter
from services import urls as urls_services
from presentation import urls as urls_presentation







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("contact/", include("contact.urls", namespace="contact")),
    path('product/', include(urls_product)),
    path('services/', include(urls_services)),
    path('presentation/', include(urls_presentation)),


]
