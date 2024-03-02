from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
 
    def __str__(self):
        return self.name
 
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
class contact_info(models.Model):
    u_email = models.EmailField()
    u_message = models.CharField(max_length=200)
    def __str__(self):
        return self.u_email
    


