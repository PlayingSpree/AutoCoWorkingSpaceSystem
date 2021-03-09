from django.urls import path, include
from rest_framework import routers

from payment.views_form import PaymentForm
from payment.views_payment import PaymentViewSet
from statapp.views import PingAPI

urlpatterns = [
    path('ping/', PingAPI.as_view(), name='ping'),
]
