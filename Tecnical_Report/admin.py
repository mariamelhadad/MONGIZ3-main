from django.contrib import admin
from .models import *
# Register your models here.
class display_technical_reports(admin.ModelAdmin):
    list_display=['Sender','__str__','Issue']
    list_display_links=['Sender','__str__','Issue']
admin.site.register(Technical_Report)