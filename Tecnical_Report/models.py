from django.db import models
from account.models import User
# Create your models here.
class Technical_Report(models.Model):
    Sender=models.OneToOneField(User,related_name='sender',on_delete=models.CASCADE,default=None)
    Issue=models.TextField(max_length=255,null=False,blank=False,default='Write your issue')
    def __str__(self):
        return self.Sender.national_id