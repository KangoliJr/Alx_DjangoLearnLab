from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView,admin_view, librarian_view, member_view
from . import views
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin_page/', admin_view, name='admin_view'),
    path('librarian_page/', librarian_view, name='librarian_view'),
    path('member_page/', member_view, name='member_view'),
]