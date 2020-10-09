from django.db import models
# Create your models here.

class Domain(models.Model):
    id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=60)
    ip = models.CharField(max_length=15)
    cname = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)

    def __str__(self):
        return '[id={},domain={},ip={},cname={}]'.format(self.id,self.domain,self.ip,self.cname,self.remark)