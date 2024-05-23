from django.contrib import admin
from .models import *
class display_reniew_id(admin.ModelAdmin):
    list_display=["Full_Name",'__str__','Birth_dt','Full_Address','Current_Job','Marital_State','Study_Field','Recent_Personal_Image']
    list_display_links=["Full_Name",'__str__','Birth_dt','Full_Address','Current_Job','Marital_State','Study_Field','Recent_Personal_Image']
class display_reniew_driving(admin.ModelAdmin):
    list_display=['Name_in_Arabic','__str__','Name_in_English','Full_Address','Job','Marital_State','Nationality','Traffic_Department','Blood_Type','Medical_Examine_Image']
    list_display_links=['Name_in_Arabic','__str__','Name_in_English','Full_Address','Job','Marital_State','Nationality','Traffic_Department','Blood_Type','Medical_Examine_Image']
# Register your models here.
admin.site.register(Personal_ID_Card,display_reniew_id)
admin.site.register(Personal_Driving_License,display_reniew_driving)