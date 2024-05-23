from django.db import models
from account.models import User

class MaritalState(models.TextChoices):
    SINGLE ='Single'
    MARRIED =  'Married'
    DIVORCED =  'Divorced'
    WIDOWED =  'Widowed'

class social_state(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,default=None,primary_key=True)
    Personel_Card = models.ImageField(upload_to='Social/social_state/Personel_Card/%y/%m/%d')
    Marital_state = models.CharField(max_length= 10, choices=MaritalState.choices, default=MaritalState.SINGLE)
    Phone_Number = models.CharField(max_length=11, default=None,unique=True,null=False,blank=False)
    Address = models.CharField(max_length=40,default=None,null=False,blank=False)
    def national_id(self):
        return f"{self.User.national_id}"

    

class Family(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,default=None,primary_key=True)
    Husband_or_Wife_Name = models.CharField(max_length=200, default=None)
    Sons_Name1 = models.CharField(max_length=100, default=None,null=True,blank=True)
    Sons_Name2 = models.CharField(max_length=100, default=None,null=True,blank=True)
    Sons_Name3 = models.CharField(max_length=100, default=None,null=True,blank=True)
    Sons_Name4 = models.CharField(max_length=100, default=None,null=True,blank=True)
    Sons_Number = models.IntegerField(null=True,blank=True)
    def national_id(self):
        return f"{self.User.national_id}"






