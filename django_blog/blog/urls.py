from django.urls import path, include
from django.contrib.auth import views as auth_views
from . views import(PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView)
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='blog_list'),
    # path('', views.blog_list, name='blog_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog_detail'),
    path('post/new/', PostCreateView.as_view(), name='blog_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='blog_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog_delete'),
    
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]