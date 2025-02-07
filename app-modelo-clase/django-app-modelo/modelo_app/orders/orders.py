from django.urls import path

from . import views

urlpatterns = [
    path("/order/list", views.indexOrders, name="order-list"),
]