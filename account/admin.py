from django.contrib import admin
from .models import *
from django.contrib.auth.models import  Group


class display_user(admin.ModelAdmin):
    list_display=['national_id','email','phone_number']
    list_display_links=['national_id','email','phone_number']
# Register your models here.
admin.site.register(User,display_user)
admin.site.unregister(Group)
admin.site.index_title="MONGIZ_App"
admin.site.site_header='Mongiz_Admin'
admin.site.site_title='Mongiz_administration'