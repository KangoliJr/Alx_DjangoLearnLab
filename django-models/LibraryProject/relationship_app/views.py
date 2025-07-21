from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request,"relationship_app/list_books.html",{"books":books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'
    
class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('register')
    template_name = 'relationship_app/register.html'

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    success_url = reverse_lazy('login')

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    success_url = reverse_lazy('logout')    