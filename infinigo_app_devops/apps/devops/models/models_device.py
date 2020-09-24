from django.db import models
from .models_user import User
from .models_user import User

# Create your models here.

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    local_ip = models.CharField(max_length=15)
    public_ip = models.CharField(max_length=15)
    ssh_port = models.CharField(max_length=6)
    environment = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=60)
    t_image = models.CharField(max_length=300,default='http://www.qq.com')
    #leader = models.ForeignKey(User, blank=True, null=True, related_name='username',on_delete=models.SET_NULL)
    leader = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '[id={},name={},local_ip={},public_ip={},ssh_port={},user={},password={},t_image={},leader={}]'.format(self.id,self.name,self.local_ip,self.public_ip,self.ssh_port,self.user,self.password,self.t_image,self.leader)






