from rest_framework import serializers
from .models import *

class PostSeraializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields =["id", "author", "title", "body"] 
