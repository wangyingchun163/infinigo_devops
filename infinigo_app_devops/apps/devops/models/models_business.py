from django.db import models
from .models_user import User
# Create your models here.

class Business(models.Model):
    id = models.AutoField(primary_key=True)  #id
    business = models.CharField(max_length=50)  #业务线
    project = models.CharField(max_length=60)   #项目名
    application = models.CharField(max_length=60)  #应用名
    deploy_dir = models.CharField(max_length=100)  #部署路径
    log_dir = models.CharField(max_length=100)   #日志路径
    local_ip = models.CharField(max_length=18)  #部署IP
    port = models.IntegerField()  #端口号
    leader = models.OneToOneField(User, to_field="id", on_delete=models.DO_NOTHING)

    def __str__(self):
        return '[id={}, business={}, project={}, application={}, leader={}, deploy_dir={}, log_dir={}, local_ip={}, port={}]'.format(self.id, self.business, self.project, self.application, self.leader, self.deploy_dir, self.log_dir,self.local_ip , self.port)