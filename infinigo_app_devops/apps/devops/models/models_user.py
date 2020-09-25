from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return '[{}]'.format(self.username).replace('[','').replace(']','')
        # return '[username={},id={}]'.format((self.username).replace('[', '').replace(']', ''), self.id)