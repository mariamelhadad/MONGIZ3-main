from django.contrib import admin
from Messages.models import *
# Register your models here.
class display_message(admin.ModelAdmin):
    list_display=['User','__str__','Header','Content']
    list_display_links=['User','__str__','Header','Content']
admin.site.register(message,display_message)