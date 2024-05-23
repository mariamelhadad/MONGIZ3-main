from rest_framework import serializers
from .models import *

class PersonalIDSerialization(serializers.ModelSerializer):
    class Meta:
        model = Personal_ID_Card
        fields='__all__'
        
        
        
class PersonalDrivingLicenseSerialization(serializers.ModelSerializer):
    class Meta:
        model = Personal_Driving_License
        fields='__all__'