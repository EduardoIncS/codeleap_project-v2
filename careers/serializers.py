from rest_framework import serializers
from .models import CareerPost

class CareerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CareerPost
        # incluímos id e created_datetime para retornar no GET
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
