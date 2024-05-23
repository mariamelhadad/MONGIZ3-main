from django.contrib import admin
from Official_Paper.models import *
# Register your models here.
class display_papers(admin.ModelAdmin):
    list_display=['User','national_id','Birth_cirtification','Id_Card','Passport','Driving_Licence']
    list_display_links=['User','national_id','Birth_cirtification','Id_Card','Passport','Driving_Licence']

admin.site.register(paper,display_papers)