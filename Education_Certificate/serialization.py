from rest_framework import serializers

from .models import *

class certification_serializer(serializers.ModelSerializer):
    class Meta:
        model = certification
        fields = ['Degree','certification']