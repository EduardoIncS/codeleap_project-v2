from rest_framework import serializers
from .models import CareerPost, PostAttachment, PostLike, PostComment

class CareerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CareerPost
        fields = ['id', 'username', 'created_datetime', 'title', 'content']

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'user', 'post', 'created_at']

class PostCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = PostComment
        fields = ['id', 'user', 'post', 'content', 'created_at']

class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ['id', 'file', 'uploaded_at']
