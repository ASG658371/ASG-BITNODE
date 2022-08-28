from dataclasses import fields
from rest_framework import serializers
from playground.models import Colleges


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colleges
        fields = '__all__'