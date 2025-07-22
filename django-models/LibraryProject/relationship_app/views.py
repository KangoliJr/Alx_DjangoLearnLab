from django.shortcuts import render, redirect
from .models import Book, Library, UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView #appleicable if I use CBV
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
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
            user = form.save()
            return redirect(reverse_lazy('login'))
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
class LoginView(LoginView):
    # success_url = reverse_lazy('login')
    pass

class LogoutView(LogoutView):
    # success_url = reverse_lazy('logout') 
    pass  
    
# Role-Based Views
def role_check(required_role):
    def check(user):
        if user.is_authenticated and hasattr(user, 'profile'):
            return user.profile.role == required_role
        return False
    return check

# @login_required
# @user_passes_test(role_check('Admin'))
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# @login_required
# @user_passes_test(role_check('Librarian'))
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# @login_required
# @user_passes_test(role_check('Member'))
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')
@login_required(login_url=reverse_lazy('login')) 
@user_passes_test(role_check('Admin'), login_url=reverse_lazy('login'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

@login_required(login_url=reverse_lazy('login')) 
@user_passes_test(role_check('Librarian'), login_url=reverse_lazy('login')) 
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

@login_required(login_url=reverse_lazy('login')) 
@user_passes_test(role_check('Member'), login_url=reverse_lazy('login')) 
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})
