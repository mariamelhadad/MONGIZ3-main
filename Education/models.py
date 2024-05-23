from django.db import models
from account.models import User
# Create your models here.

class educational_state (models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,default=None,primary_key=True)
    Name = models.CharField(max_length=200, default=None)
    Schools = models.CharField(max_length=200, default=None,null=False,blank=False)
    Faculty= models.CharField(max_length=200, default=None,null=True,blank=True)
    University = models.CharField(max_length=200, default=None,null=True,blank=True)

    def national_id(self):
        return f"{self.User.national_id}"



