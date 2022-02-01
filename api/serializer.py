from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    this seriliazer for models post to create, update, delete
    """
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'slug']


