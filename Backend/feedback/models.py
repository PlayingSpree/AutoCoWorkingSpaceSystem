from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from authapp.models import User


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '[Feedback id:{}] Rating: {} '.format(self.id, self.rating)


class ProblemType(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()

    def __str__(self):
        return '[ProblemType id:{}] Name: {} '.format(self.id, self.name)


class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(ProblemType, on_delete=models.CASCADE)
    severity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        severity_text = 'Not Set' if self.severity is None else self.severity
        return '[Problem id:{}] severity: {} '.format(self.id, severity_text)
