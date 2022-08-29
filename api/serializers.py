from dataclasses import fields
from rest_framework import serializers
from playground.models import *


class CollegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colleges
        fields = '__all__'
    
class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
         