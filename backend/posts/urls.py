from django.urls import path
from .views import (
    Posts_GetPost_APIView, 
    Post_PatchDelete_APIView, 

    PostComments_Get_APIView,
    Comment_Post_APIView,
    Comment_PatchDelete_APIView
)

urlpatterns = [
    path('careers/', Posts_GetPost_APIView.as_view(), name='posts'),
    path('careers/<int:id>/', Post_PatchDelete_APIView.as_view(), name='post'),

    path('careers/<int:post_id>/comment/', Comment_Post_APIView.as_view(), name='comments'),
    path('careers/<int:post_id>/comments/', PostComments_Get_APIView.as_view(), name='comment'),
    path('careers/comment/<int:id>/', Comment_PatchDelete_APIView.as_view(), name='comment-update'),
]