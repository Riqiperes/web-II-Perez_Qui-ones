from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def indexOrders(request):
    return render(request, 'orders/home.html')


def paymentsByOrder(request):
    return render(request, 'orders/payments.html')


def orders(request):
    return render(request, 'orders/index.html')