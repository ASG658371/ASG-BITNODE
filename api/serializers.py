from dataclasses import fields
from rest_framework import serializers
from playground.models import test

class testSerializer(serializers.ModelSerializer):
    class Meta:
        model=test
        fields='__all__'