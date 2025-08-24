from django.urls import path, include
from django.contrib.auth import views as auth_views
from . views import(PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, CommentCreateView, CommentUpdateView, CommentDeleteView)
from . import views as blog_app_views
# from . import views 
# urlpatterns = [
#     path('', PostListView.as_view(), name='blog_list'),
#     path('post/<int:pk>/', PostDetailView.as_view(), name='blog_detail'),
#     path('post/new/', PostCreateView.as_view(), name='blog_create'),
#     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog_update'),
#     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog_delete'),
    
#     path('register/', views.register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
#     path('profile/', views.profile, name='profile'),
    

#     path('posts/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
#     path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
#     path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
# ]

urlpatterns = [
    # Blog post URLs
    path('', PostListView.as_view(), name='blog_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='blog_detail'),
    path('posts/new/', PostCreateView.as_view(), name='blog_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='blog_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='blog_delete'),

    # Authentication URLs
    path('register/', blog_app_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', blog_app_views.profile, name='profile'),

    # Comment URLs (Corrected to match checker's requirements)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]