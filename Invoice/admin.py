from django.contrib import admin
from .models import Customer, Product, InvoiceItem, Invoice

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
