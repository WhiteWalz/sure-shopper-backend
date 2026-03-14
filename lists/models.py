from django.db import models

# Create your models here.
class List(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('products.Product')

    def __str__(self):
        return self.id