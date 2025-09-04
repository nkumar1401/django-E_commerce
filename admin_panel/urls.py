from django.urls import path
from products.views import admin_product_list, admin_product_create
from orders.views import admin_order_list

urlpatterns = [
    path("products/", admin_product_list, name="admin_products"),
    path("products/create/", admin_product_create, name="admin_product_create"),
    path("orders/", admin_order_list, name="admin_orders"),
]
