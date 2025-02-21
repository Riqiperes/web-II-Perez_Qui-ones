from django.urls import path

from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path("home", views.indexOrders, name="indexOrders")
]