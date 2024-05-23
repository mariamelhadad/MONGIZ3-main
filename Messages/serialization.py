from rest_framework import serializers
from .models import *


class msg_serializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ['Header','Content']
