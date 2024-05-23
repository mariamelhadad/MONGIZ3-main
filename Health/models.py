from django.db import models
from account.models import User


class Blood_type(models.TextChoices):
    A_PLUS = "A+",
    A_MINUS = "A-",
    B_PLUS = "B+",
    B_MINUS = "B-",
    AB_PLUS = "AB+",
    AB_MINUS = "AB-",  
    O_PLUS = "O+" , 
    O_MINUS = "O-",


class health_state (models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,default=None,primary_key=True)
    Name = models.CharField(max_length=200, default=None)
    Age=models.IntegerField(null=False,blank=False)
    Blood_Quarter = models.CharField(max_length=3, choices=Blood_type.choices, default=None)
    Health_Problem = models.TextField(max_length=500, default=None,null=True,blank=True)

    def national_id(self):
        return f"{self.User.national_id}"





