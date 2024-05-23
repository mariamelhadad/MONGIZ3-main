from django.db import models
from account.models import User

class work_career(models.Model):
    Sender=models.OneToOneField(User,on_delete=models.CASCADE,default=None,primary_key=True)
    Current_Jop = models.CharField(max_length=200, default=None,null=False,blank=False)
    Campanies = models.TextField()
    Other = models.TextField(default=None)

    def __str__(self):
      return self.Sender.national_id
    