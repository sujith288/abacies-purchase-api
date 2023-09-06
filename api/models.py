from django.db import models
from django.utils import timezone
import uuid

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    available_product_stock = models.PositiveIntegerField(default=25000)

class Purchase(models.Model):
    purchase_id =models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchased_qty = models.PositiveIntegerField()
    csv_exported = models.BooleanField(default=False)
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created          = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.product_name

class Refill(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fillup_quantity = models.PositiveIntegerField()
    created          = models.DateTimeField(default=timezone.now)
    
