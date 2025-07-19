from django.urls import path
from .views import PostsCollectionAPIView, PostItemAPIView

urlpatterns = [
    path('careers/', PostsCollectionAPIView.as_view(), name='posts-collection'),
    path('careers/<int:id>/', PostItemAPIView.as_view(), name='post-item'),
]