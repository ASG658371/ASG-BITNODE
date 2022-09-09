from dataclasses import fields
from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField
from playground.models import *


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
    
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class UploadSerializer(serializers.Serializer):
    file_uploaded =  FileField()
    class Meta:
        fields = ['file_uploaded']


         