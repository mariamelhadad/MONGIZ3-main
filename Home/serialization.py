from rest_framework import serializers
from Home.models import Home_page

class homeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home_page
        fields =['Name','Nationality','Marital_state','Blood_quarter','Address','BirthDate']
