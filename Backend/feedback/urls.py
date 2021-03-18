from django.urls import path, include
from rest_framework import routers

from feedback.views_feedback import FeedbackViewSet
from feedback.views_problem import ProblemViewSet, ProblemTypeViewSet
from feedback.views_stats import FeedbackStat
from payment.views_form import PaymentForm
from payment.views_payment import PaymentViewSet
from payment.views_stats import PaymentStat

router = routers.DefaultRouter()
router.register('problem/type', ProblemTypeViewSet)
router.register('problem', ProblemViewSet)
router.register('', FeedbackViewSet)

urlpatterns = [
    path('stat/', FeedbackStat.as_view()),
    path('', include(router.urls))
]
