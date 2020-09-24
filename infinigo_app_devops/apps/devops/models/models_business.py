from django.db import models
from .models_user import User
# Create your models here.

class Business(models.Model):
    id = models.AutoField(primary_key=True)
    business = models.CharField(max_length=50)  #业务线
    project = models.CharField(max_length=60)   #项目名
    application = models.CharField(max_length=60)  #应用名
    #leader = models.ForeignKey(User, blank=True, null=True , related_name='username', on_delete=models.SET_NULL)   #负责人
    leader = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)   #负责人
    def __str__(self):
        return '[id={},business={},project={},application={},leader={}]'.format(self.id,self.business,self.project,self.application,self.leader)