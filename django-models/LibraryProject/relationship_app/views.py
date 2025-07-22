from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView #appleicable if I use CBV
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request,"relationship_app/list_books.html",{"books":books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'
    
# def register(request):
#     return RegisterView.as_view(template_name='relationship_app/register.html')(request)
# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('register')
#  also correct 
# using function based views
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
class LoginView(LoginView):
    success_url = reverse_lazy('login')

class LogoutView(LogoutView):
    success_url = reverse_lazy('logout')   
    
# Role-Based Views
def check_role(role_name):
    def decorator(user):
        return user.is_authenticated and user.userprofile.role==role_name
    return decorator

@login_required
@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(check_role('Librarian'))
def admin_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(check_role('Member'))
def admin_view(request):
    return render(request, 'member_view.html')