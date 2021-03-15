from django.urls import path, include
from rest_framework import routers

from authapp.views import UserViewSet
from feedback.views_feedback import FeedbackViewSet
from feedback.views_problem import ProblemViewSet, ProblemTypeViewSet
from payment.views_form import PaymentForm
from payment.views_payment import PaymentViewSet
from payment.views_stats import PaymentStat

router = routers.DefaultRouter()
router.register('admin/user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
