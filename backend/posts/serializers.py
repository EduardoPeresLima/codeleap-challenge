from rest_framework import serializers
from .models import Post, Comment

################################## POST Serializers ########################################
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
        read_only_fields = ['id', 'created_datetime']

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content']

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'created_datetime', 'title', 'content']
        read_only_fields = ['id', 'created_datetime', 'username']

################################## COMMENT Serializers ########################################
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_datetime', 'parent_comment', 'username']
        read_only_fields = ['id', 'created_datetime', 'post']

class CommentRecursiveListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'username', 'content', 'created_datetime', 'replies']

    def get_replies(self, obj):
        # Find all of the comment's comments
        children = obj.replies.all()
        return CommentRecursiveListSerializer(children, many=True).data

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'username', 'content', 'created_datetime']
        read_only = ['id', 'username', 'created_datetime']