"""Serializer for the student API View."""
from rest_framework import serializers
from core.models import StudentRecord

class StudentRecordSerializer(serializers.ModelSerializer):
    """Serializer for the student record object."""
    class Meta:
        model = StudentRecord
        fields = '__all__'