from django.contrib import admin
from .models import Product, CartItem, contact_info

# Register your models here.



admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(contact_info)


