from django.contrib import admin
from .models import Product, CartItem, PurchaseRecord, PurchaseItem

# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(PurchaseRecord)
admin.site.register(PurchaseItem)
