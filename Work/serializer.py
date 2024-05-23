from rest_framework import serializers
from Work.models import work_career

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = work_career
        fields = '__all__'