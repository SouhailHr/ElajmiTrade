from django.conf.urls import url, include
from django.urls import path
from .views import all_products,  product_filter

app_name = "product"


urlpatterns = [
    path('', all_products , name="products"),
    path(r'^(?P<category>\w+)/$', product_filter, name="product-filter"),

]