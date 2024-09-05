from django.db import models
from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField
)

class MeanOfTransportation(models.Model):
    TRANSPORTATION_CHOICES = [
        ('Rail', 'Rail'),
        ('Road', 'Road'),
        ('Combination', 'Combination'),
    ]
    mean_of_transportation = models.CharField(max_length=100,
        choices=TRANSPORTATION_CHOICES
    )
    def __str__(self):
        return self.mean_of_transportation

class Lead(models.Model):
    TRANSPORTATION_CHOICES = [
        ('Rail', 'Rail'),
        ('Road', 'Road'),
        ('Combination', 'Combination'),
    ]
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    preferred_mean_of_transportation = models.ForeignKey(
        MeanOfTransportation,on_delete=DO_NOTHING
    )
    def __str__(self):
        return self.customer_name+""+str(self.amount)
