from django.urls import path
from .views import PostsCollectionAPIView, PostItemAPIView

urlpatterns = [
    path('', PostsCollectionAPIView.as_view(), name='posts-collection'),
    path('<int:id>/', PostItemAPIView.as_view(), name='post-item'),
]