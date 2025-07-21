from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.RegisterView.as_view(template_name = 'relationship_app/register.html'), name='register'),
    path('login/', views.LoginView.as_view(template_name = 'relationship_app/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name = 'relationship_app/logout.html'), name='logout'),
]
