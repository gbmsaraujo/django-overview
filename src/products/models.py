from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        decimal_places=2, max_digits=10000, blank=False, null=False
    )
    summary = models.TextField(default='This is cool!')
    featured = models.BooleanField(default=True)
