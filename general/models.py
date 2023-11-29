from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=250, null=False, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
