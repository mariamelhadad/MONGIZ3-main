from django.contrib import admin
from .models import educational_state
class display_education(admin.ModelAdmin):
    list_display=['Name','national_id','Schools','Faculty','University']
    list_display_links=['Name','national_id','Schools','Faculty','University']
admin.site.register(educational_state,display_education)


