from rest_framework import serializers
from Health.models import health_state 

class healthstate_serializer(serializers.ModelSerializer):
    class Meta:
        model = health_state
        fields = ['Name','Age','Blood_Quarter','Health_Problem']



