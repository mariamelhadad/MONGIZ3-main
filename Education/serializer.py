from rest_framework import serializers
from Education.models import educational_state 

class educational_state_serializer(serializers.ModelSerializer):
    class Meta:
        model = educational_state 
        fields = ['Name','Schools','Faculty','University']

