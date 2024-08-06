from django.db import models
from Test_IT_Solutions.consts import FUEL_CHOICES, TRANSMISSION_CHOICES


class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

