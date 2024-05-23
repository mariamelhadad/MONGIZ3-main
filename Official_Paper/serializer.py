from rest_framework import serializers
from Official_Paper.models import paper

class papersSerializer(serializers.ModelSerializer):
    class Meta:
        model = paper
        fields = ['Birth_cirtification','Id_Card','Passport','Driving_Licence']