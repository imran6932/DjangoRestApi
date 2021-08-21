from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    '''Student API Model Serializer'''
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']

