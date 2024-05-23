from django.db import models
from account.models import User
# Create your models here.
class certification(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE,default=None,primary_key=True)
    Degree = models.CharField(max_length=100 , default=None)
    certification = models.ImageField(upload_to='Education/certification/Passport_Photo/%y/%m/%d',null=True)
    def national_id(self):
        return f"{self.User.national_id}"