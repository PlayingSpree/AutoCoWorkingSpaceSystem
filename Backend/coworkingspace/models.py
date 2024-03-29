import random
from datetime import timedelta

from django.db import models
from django.utils import timezone

from authapp.models import User
from payment.models import Payment


class CoworkingSpacePackage(models.Model):
    name = models.CharField(max_length=64)
    detail = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return '[Package id:{}] {}'.format(self.id, self.name)


class CoworkingSpaceSubscription(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(CoworkingSpacePackage, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    is_canceled = models.BooleanField(default=False)
    qr_key = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_qr_key(self):
        return str(self.qr_key)

    def is_in_subscription_date(self, date=timezone.localdate()):
        return not self.is_canceled and self.date_start <= date <= self.date_end

    def save(self, *args, **kwargs):
        self.qr_key = random.randint(0, 99999)
        super().save(*args, **kwargs)

    def __str__(self):
        return '[PackageSubscription id:{}{}] {} to {} by {} at {}'.format(self.id,
                                                                           ' CANCELED' if self.is_canceled else '',
                                                                           self.date_start, self.date_end, self.user,
                                                                           self.package)
