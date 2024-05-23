from django.contrib import admin
from .models import social_state , Family
class display_social_state(admin.ModelAdmin):
    list_display=['User','national_id','Phone_Number','Marital_state']
    list_display_links=['User','national_id','Phone_Number','Marital_state']
class display_social_family(admin.ModelAdmin):
    list_display=['User','national_id','Husband_or_Wife_Name','Sons_Name1','Sons_Name2','Sons_Name3','Sons_Name4','Sons_Number']
    list_display_links=['User','national_id','Husband_or_Wife_Name','Sons_Name1','Sons_Name2','Sons_Name3','Sons_Name4','Sons_Number']
admin.site.register(social_state,display_social_state)
admin.site.register(Family,display_social_family)

