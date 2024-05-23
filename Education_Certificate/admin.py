from django.contrib import admin
from .models import *
# Register your models here.
class display_education_certificates(admin.ModelAdmin):
    list_display=['User','national_id','Degree']
    list_display_links=['User','national_id','Degree']
# Register your models here.
admin.site.register(certification,display_education_certificates)