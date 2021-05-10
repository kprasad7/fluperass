from rest_framework import serializers
from app3.models import Category

class Cat_serializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = "__all__"