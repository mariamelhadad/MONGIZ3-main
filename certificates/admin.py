from django.contrib import admin
from .models import *

# Register your models here.
class display_Personal_Info(admin.ModelAdmin):
    list_display=['Full_Name','national_id','Profession','Address','City','state']
    list_display_links=['Full_Name','national_id','Profession','Address','City','state']
class display_Expereince(admin.ModelAdmin):
    list_display=['national_id','Company','Employer','Company_Address','Start_Date','Finish_Date','Currently_work_here']
    list_display_links=['national_id','Company','Employer','Company_Address','Start_Date','Finish_Date','Currently_work_here']
class display_Education(admin.ModelAdmin):
    list_display=['national_id','School_Name','School_Location','Degree_Program','Degree_Program','Field_Of_Study','Graduation_Month_and_Year']
    list_display_links=['national_id','School_Name','School_Location','Degree_Program','Degree_Program','Field_Of_Study','Graduation_Month_and_Year']
class display_Technical_Skill(admin.ModelAdmin):
    list_display=['national_id','Skill1','Skill2','Skill3','Skill4','Skill5']
    list_display_links=['national_id','Skill1','Skill2','Skill3','Skill4','Skill5']
class display_Contact_Info(admin.ModelAdmin):
    list_display=['national_id','Phone_Number','Linkedin_Profile_Link','Twitter_Profile_Link','GitHub_Profile_Link','Portfolio_Link']
    list_display_links=['national_id','Phone_Number','Linkedin_Profile_Link','Twitter_Profile_Link','GitHub_Profile_Link','Portfolio_Link']
admin.site.register(Technical_Skill,display_Technical_Skill)
admin.site.register(Expereince,display_Expereince)
admin.site.register(Education,display_Education)
admin.site.register(Personal_Info,display_Personal_Info)
admin.site.register(Contact_Info,display_Contact_Info)