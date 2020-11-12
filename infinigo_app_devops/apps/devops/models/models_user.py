from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50)

    def __str__(self):
        # return '[username={}]'.format(self.username)
        # return self.username
        return '[id={},username={}]'.format(self.id, self.username)