from django.contrib import admin

# Register your models here.
from feedback.models import Feedback, ProblemType, Problem

admin.site.register(Feedback)
admin.site.register(ProblemType)
admin.site.register(Problem)
