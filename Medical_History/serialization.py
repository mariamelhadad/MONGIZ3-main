from rest_framework import serializers
from .models import *

class medicalhistoryserialization(serializers.ModelSerializer):
    class Meta:
        model = medicalhistory
        fields=['Name','Age','Chronic_Diseases','Another_Diseases']