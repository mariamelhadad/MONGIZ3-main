from django.db import models
from Social.models import social_state
from account.models import User
class paper(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Birth_cirtification = models.ImageField(upload_to='offcial_papers/Birth_cirtification/%y/%m/%d')
    Id_Card = models.ImageField(upload_to='offcial_papers/Id_Card_Photo/%y/%m/%d')
    Passport = models.ImageField(upload_to='offcial_papers/Passport_Photo/%y/%m/%d')
    Driving_Licence = models.ImageField(upload_to='offcial_papers/Driving_Licence_Photo/%y/%m/%d')
    def national_id(self):
        return f"{self.User.national_id}"