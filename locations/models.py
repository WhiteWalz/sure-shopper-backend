from django.db import models

# Create your models here.
class Location(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    localPoint = models.PointField()


    def __str__(self):
        return self.id