from django.contrib import admin

# Register your models here.
from coworkingspace.models import CoworkingSpacePackage, CoworkingSpaceSubscription

admin.site.register(CoworkingSpacePackage)
admin.site.register(CoworkingSpaceSubscription)
