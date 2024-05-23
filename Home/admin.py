from django.contrib import admin
from .models import Home_page
class display_Home(admin.ModelAdmin):
    list_display=['Name','national_id']
    list_display_links=['Name','national_id']
admin.site.register(Home_page,display_Home)