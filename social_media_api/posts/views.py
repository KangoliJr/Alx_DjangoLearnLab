from django.shortcuts import render
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, filters, permissions, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
# Create your views here.
class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user

class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author__username']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        post = Post.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        feed_data = [
            {
                "id": posts.id,
                "author": posts.author.username,
                "title": posts.title,
                "content": posts.content,
                "created_at": posts.created_at,
            }
            for posts in posts
        ]
        return Response(feed_data)

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        if post.likes.filter(user=request.user).exists():
            post.likes.filter(user=request.user).delete()
            return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
        else:
            Like.objects.create(post=post, user=request.user)
            
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb='liked',
                    target_content_type=ContentType.objects.get_for_model(Post),
                    target_object_id=post.pk
                )
            
            return Response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)