
# Create your models here.
from django.db import models


# Create your models here.
class Kitchen(models.Model):
  product = models.CharField(max_length=100, unique=True)
  product_description = models.CharField(max_length=500)
  product_image = models.ImageField(upload_to='kitchen/')
  price = models.PositiveIntegerField(null=False, blank=False)

  def _str_(self):
    return self.product
  
class Sale(models.Model):
  product = models.ForeignKey(Kitchen, on_delete=models.CASCADE)
  price = Kitchen.price
  quantity = models.PositiveIntegerField(default=0)
  time = models.DateTimeField(auto_now_add=True)

  def total_price(self):
    return self.price * self.quantity
  
  def _str_(self):
    # return str(self.product + "@" + str(self.time))
    return f"{self.product} + {self.time}"