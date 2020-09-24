from django.db import models

# Create your models here.

class Supplier(models.Model):
    company = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    idc_address = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    contact_phone = models.CharField(max_length=20)
    assistant = models.CharField(max_length=10)
    assistant_phone = models.CharField(max_length=20)