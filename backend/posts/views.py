from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Post, Comment
from .serializers import (
    PostCreateSerializer,
    PostListSerializer,
    PostUpdateSerializer,

    CommentCreateSerializer,
    CommentRecursiveListSerializer,
    CommentUpdateSerializer
)

################## POST ######################
class Posts_GetPost_APIView(APIView):
    def get(self, request):
        all_posts_objects = Post.objects.all()
        serializer = PostListSerializer(all_posts_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            # Re-serializes to garantee consistent output
            out = PostCreateSerializer(post)
            return Response(out.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Post_PatchDelete_APIView(APIView):

    def patch(self, request, id):
        post = get_object_or_404(Post, pk=id)
        serializer = PostUpdateSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################# COMMENT ####################
class Comment_Post_APIView(APIView):
    def post(self, request, post_id):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(post_id=post_id)
            # Re-serializes to garantee consistent output
            out = CommentCreateSerializer(post)
            return Response(out.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostComments_Get_APIView(APIView):
    def get(self, request, post_id):
        root_comments = Comment.objects.filter(post_id=post_id, parent_comment__isnull=True)
        serializer = CommentRecursiveListSerializer(root_comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Comment_PatchDelete_APIView(APIView):
    def patch(self, request, id):
        comment = get_object_or_404(Comment, pk=id)
        serializer = CommentUpdateSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = get_object_or_404(Comment, pk=id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
