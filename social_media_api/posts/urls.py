from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView,LikeView,UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

posts_router = NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = router.urls + posts_router.urls
urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user-feed'),
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
    path('posts/<int:pk>/like/', LikeView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]