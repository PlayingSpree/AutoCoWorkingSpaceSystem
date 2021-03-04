from django.urls import path
from payment.views_form import PaymentForm
from payment.views_process import ProcessView

urlpatterns = [
    path('form/', PaymentForm.as_view(), name='payment_form'),
    path('', ProcessView.as_view(), name='payment_process'),
]
