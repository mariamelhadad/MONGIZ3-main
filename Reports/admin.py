from django.contrib import admin

from Reports.models import Report
class display_reports(admin.ModelAdmin):
    list_display=['Name','national_id','Complaints']
    list_display_links=['Name','national_id','Complaints']
admin.site.register(Report,display_reports)
