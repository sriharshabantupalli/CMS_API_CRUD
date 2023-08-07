from rest_framework import serializers
from .models import Post, Like

class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'content', 'creation_date', 'owner', 'like_count']

    def get_like_count(self, obj):
        return obj.like_set.count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'like_date']