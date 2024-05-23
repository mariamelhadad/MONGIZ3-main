from django.db import models
from account.models import User
# Create your models here.
class medicalhistory(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,default=None,primary_key=True)
    Name=models.CharField(max_length=50,default=None,null=False,blank=False)
    Age=models.IntegerField(default=None,null=False,blank=False)
    Chronic_Diseases=models.TextField(max_length=255,default=None,null=True,blank=True)
    Another_Diseases=models.TextField(max_length=255,default=None,null=True,blank=True)
    def national_id(self):
        return f"{self.User.national_id}"