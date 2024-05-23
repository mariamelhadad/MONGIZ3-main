from rest_framework  import serializers
from  .models import *

class PersonalInfoserialization(serializers.ModelSerializer):
    class Meta:
        model= Personal_Info
        fields='__all__'
class Expereinceserialization(serializers.ModelSerializer):
    class Meta:
        model= Expereince
        fields='__all__'
        
class Technicalskillsserialization(serializers.ModelSerializer):
    class Meta:
        model= Technical_Skill
        fields='__all__'
        
class  Educationserialization(serializers.ModelSerializer):
    class Meta:
        model= Education
        fields='__all__'        
class  Contact_Infoserialization(serializers.ModelSerializer):
    class Meta:
        model= Contact_Info
        fields='__all__'
        