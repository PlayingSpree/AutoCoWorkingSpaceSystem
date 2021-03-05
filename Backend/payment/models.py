from django.db import models
import omise

omise.api_secret = 'skey_test_5lruxk5hrhpwbu5trj1'


class Payment(models.Model):
    charge_token = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    amount = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[Payment id:{}] Amount: {} Status: {}'.format(self.id, self.amount, self.status)

    @staticmethod
    def pay(card_token, amount):
        payment = None
        try:
            charge = omise.Charge.create(
                amount=amount * 100,
                currency="THB",
                card=card_token,
            )
            payment = Payment.objects.create(charge_token=charge.id, status=charge.status, amount=charge.amount)
        finally:
            return payment
