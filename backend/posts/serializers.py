from rest_framework import serializers
from .models import Post

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
        read_only_fields = ['id', 'created_datetime']
        extra_kwargs = {
            'username': {'error_messages': {'required': 'Informe o username.'}},
            'title': {'error_messages': {'required': 'Informe o título.'}},
            'content': {'error_messages': {'required': 'Informe o conteúdo.'}},
        }


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content']


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']