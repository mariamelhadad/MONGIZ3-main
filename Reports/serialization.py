from rest_framework import serializers
from Reports.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'