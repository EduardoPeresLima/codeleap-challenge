from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import (
    PostCreateSerializer,
    PostListSerializer,
    PostUpdateSerializer,
)


class PostsCollectionAPIView(APIView):
    """
    GET /         → Fetch all posts (username, title, content)
    POST /        → Create a post e return it (id, username, created_datetime, title, content)
    """

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

class PostItemAPIView(APIView):
    """
    PATCH /<id>/  → Update (title/content) and returns (title, content)
    DELETE /<id>/ → Deletes the Post and return an empty body (204)
    """

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostUpdateSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)