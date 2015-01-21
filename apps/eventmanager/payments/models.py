# models.py- Payments
from apps.eventmanager.registrant.models import *
from django.db import models

class Payments(models.Model):
    # tie into payments api
    name = models.CharField(max_lenth=100)
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    institution = models.CharField(max_length=100)
    paymentType = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=50, decimal_places=2)

    registrant = models.ForeignKey(Registrant)


