from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    available_product_stock = models.PositiveIntegerField(default=25000)

class Purchase(models.Model):
    purchase_id = models.CharField(max_length=255, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchased_qty = models.PositiveIntegerField()

class Refill(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fillup_quantity = models.PositiveIntegerField()




