from django.db import models
from  account.models import User
import datetime
# Create your models here.

class Skills(models.TextChoices):
    Html="Html"
    Css="Css"
    Javascript= "Javascript"
    React= "React"
    Angular="Angular"
    Vue = 'Vue.js'
    Photoshop='Photoshop'
    Illustrator= "Illustrator"
    Python= "Python"
    Flask= "Flask"
    Django="Django"
    Nodejs= "Node.js"
    C="C#"
    MongoDB= "MongoDB"
    SQl= "SQL"
    PostgressSQL= "PostgreSQL"
    Git= "Git"
    Github= "Github"
    Power_BI= "Power BI"
    UIUX= "UI/UX Designing"
    Figma= "Figma"
    Xd= "Adobe XD"
    Excel= "Microsoft Excel" 
    Word= "Microsoft Word"  
    PowerPoint= "Microsoft Power Point"
    Content_Creator= "Content Creator"
    Writing= "Writing"
    Translation= "Translation"
    Editing= "Editing"
    Video_Editing= "Video Editing"
    Pr="Adobe Pr"
    
class cities(models.TextChoices):   
     Cairo='Cairo'
     Giza='Giza'
     Aswan='Aswan'
     Alexandria='Alexandria'
     Amarna_city='Amarna city'
     Elephantine_city='Elephantine city'
     Days_cairo_tour_packages='Days cairo tour packages'
     Damietta='Damietta'
     Luxor='Luxor'
     Heliopolis_city='Heliopolis city'
     Qena='Qena'
     Zagazig='Zagazig'
     Fayoum='Fayoum'
     Minya='Minya'
     Al_maḩallah_al_kubrá='Al maḩallah al kubrá'
     Mansoura='Mansoura'
     
class state(models.TextChoices):   
    Egypt='Egypt'  
     
    
class Personal_Info(models.Model):
    Sender=models.OneToOneField(User,on_delete=models.CASCADE)
    Full_Name=models.CharField(max_length=100,default=" ",null=False,blank=False)
    Email=models.EmailField(unique=True,default=" ")
    Profession=models.CharField(max_length=100,default=" ",null=False,blank=False)
    Address=models.CharField(max_length=100,default=" ",null=False,blank=False)
    City=models.CharField(max_length=100,choices=cities.choices,default=" ",null=False,blank=False)
    state=models.CharField(max_length=100,choices=state.choices,default="Egypt",null=False,blank=False)
    def national_id(self) -> str:
        return f'{self.Sender.national_id}'
    
    
class Expereince(models.Model):
       Sender=models.OneToOneField(User,on_delete=models.CASCADE)
       Company=models.CharField(max_length=100,default=" ",null=False,blank=False)
       Employer=models.CharField(max_length=100,default=" ",null=False,blank=False)
       Role=models.CharField(max_length=100,default=" ",null=False,blank=False)
       Company_Address=models.CharField(max_length=100,default=" ",null=False,blank=False)
       Start_Date=models.DateField(null=False,blank=False)
       Finish_Date=models.DateField(null=False,blank=False)
       Currently_work_here=models.BooleanField(default=False)
       def national_id(self) -> str:
        return f'{self.Sender.national_id}'
       
       
        
class Education(models.Model):
    Sender=models.OneToOneField(User,on_delete=models.CASCADE)
    School_Name=models.CharField(max_length=100,default=" ",null=False,blank=False)
    School_Location=models.CharField(max_length=100,default=" ",null=False,blank=False) 
    Degree_Program=models.CharField(max_length=100,default=" ",null=False,blank=False)      
    Field_Of_Study=models.CharField(max_length=100,default=" ",null=False,blank=False)      
    Graduation_Month_and_Year=models.DateField(default=datetime.date.today(),null=True)
    def national_id(self) -> str:
        return f'{self.Sender.national_id}'
      
          
class Technical_Skill(models.Model):      
     Sender=models.OneToOneField(User,on_delete=models.CASCADE)
     Skill1=models.CharField(max_length=50,choices=Skills.choices,unique=True)
     Skill2=models.CharField(max_length=50,choices=Skills.choices,unique=True)
     Skill3=models.CharField(max_length=50,choices=Skills.choices,unique=True)
     Skill4=models.CharField(max_length=50,choices=Skills.choices,unique=True)
     Skill5=models.CharField(max_length=50,choices=Skills.choices,unique=True)
     def national_id(self) -> str:
        return f'{self.Sender.national_id}'
     
class Contact_Info(models.Model):
      Sender=models.OneToOneField(User,on_delete=models.CASCADE)
      Phone_Number=models.CharField(max_length=11)   
      Linkedin_Profile_Link=models.URLField(max_length=100,default="https/",null=False,blank=False,unique=True)    
      Twitter_Profile_Link=models.URLField(max_length=100,default="https/",null=False,blank=False,unique=True)    
      GitHub_Profile_Link=models.URLField(max_length=100,default="https/",null=False,blank=False,unique=True)    
      Portfolio_Link=models.URLField(max_length=100,default="https/",null=False,blank=False,unique=True) 
      def national_id(self) -> str:
        return f'{self.Sender.national_id}'


         