from django.db import models
from datetime import datetime

# Create your models here.
#model for the product
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)#Pepsi
    image = models.TextField()#pepsi image
    price = models.FloatField()
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
#model for the transaction
class Transaction(models.Model):
    amount = models.FloatField()
    tx_id = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)#Tazer
    phone = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255, default='Refactory')
    date = models.DateTimeField(default=datetime.now)
    method = models.TextChoices("Bank","Cash","Mobile Money","VISA")# anything out of these options listed in the method model can't  be changed.you make e a default.


    