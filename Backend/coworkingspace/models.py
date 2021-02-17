from django.db import models
from authapp.models import User


class CoworkingSpacePackage(models.Model):
    name = models.CharField(max_length=64)
    detail = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return '[Package id:{}] {}'.format(self.id, self.name)


class CoworkingSpaceSubscription(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(CoworkingSpacePackage, on_delete=models.SET_NULL, null=True)
    is_canceled = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[PackageSubscription id:{}{}] {} to {} by {} at {}'.format(self.id,
                                                                           ' CANCELED' if self.is_canceled else '',
                                                                           self.date_start, self.date_end, self.user,
                                                                           self.package)
