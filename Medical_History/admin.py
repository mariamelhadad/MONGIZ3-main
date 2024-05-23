from django.contrib import admin
from .models import *
# Register your models here.
class display_medical_history(admin.ModelAdmin):
    list_display=['Name','national_id','Age','Chronic_Diseases']
    list_display_links=['Name','national_id','Age','Chronic_Diseases']
admin.site.register(medicalhistory,display_medical_history)