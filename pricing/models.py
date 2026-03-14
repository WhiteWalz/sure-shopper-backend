from django.db import models

# Create your models here.
class Price(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.product.name}: {self.price}"