from rest_framework import serializers
from .models import CareerPost, PostLike

class CareerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CareerPost
        fields = ['id', 'username', 'created_datetime', 'title', 'content']

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'user', 'post', 'created_at']