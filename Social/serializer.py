from rest_framework import serializers
from Social.models import social_state , Family


class social_state_serializer(serializers.ModelSerializer):
    class Meta:
        model = social_state
        fields = ['Personel_Card','Marital_state','Phone_Number','Address']

class Family_serializer(serializers.ModelSerializer):
    class Meta:
        model= Family
        fields = ['Husband_or_Wife_Name','Sons_Name1','Sons_Name2','Sons_Name3','Sons_Name4','Sons_Number']