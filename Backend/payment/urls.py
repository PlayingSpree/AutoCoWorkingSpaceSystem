from django.urls import path, include
from rest_framework import routers

from payment.views_form import PaymentForm
from payment.views_payment import PaymentViewSet

router = routers.DefaultRouter()
router.register('', PaymentViewSet)

urlpatterns = [
    path('form/', PaymentForm.as_view(), name='payment_form'),
    path('', include(router.urls)),
]
