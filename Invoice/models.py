from django.db import models


class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)


class Product(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Quantity = models.PositiveIntegerField()
    Tax = models.DecimalField(max_digits=5, decimal_places=2)


class Invoice(models.Model):
    Invoice_ID = models.AutoField(primary_key=True)
    Date = models.DateField()
    Payment_method = models.CharField(max_length=50)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Products = models.ManyToManyField(Product, through='InvoiceItem')


class InvoiceItem(models.Model):
    Invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField()
