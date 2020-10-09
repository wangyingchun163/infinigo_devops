from django.db import models

# Create your models here.

class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    idc_address = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    contact_phone = models.CharField(max_length=20)
    assistant = models.CharField(max_length=10)
    assistant_phone = models.CharField(max_length=20)

    def __str__(self):
        return '[id={},company={},address={},idc_address={},contact={},contact_phone={},assistant={},assistant_phone={}]'\
            .format(self.id,self.company,self.address,self.idc_address,self.contact,self.contact_phone,self.assistant,self.assistant_phone)