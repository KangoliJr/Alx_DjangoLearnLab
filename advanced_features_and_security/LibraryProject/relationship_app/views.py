from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Library, UserProfile, Author
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView #appleicable if I use CBV
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django import forms
from django.contrib.auth.decorators import permission_required



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
    success_url = reverse_lazy('login')


class LogoutView(LogoutView):
    success_url = reverse_lazy('logout') 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author']
# Role-Based Views
def role_check(required_role):
    def check(user):
        if user.is_authenticated and hasattr(user, 'profile'):
            return user.profile.role == required_role
        return False
    return check

@login_required
@user_passes_test(role_check('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(role_check('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(role_check('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



@permission_required('relationship_app.can_add_book', login_url=reverse_lazy('login'))
@login_required(login_url=reverse_lazy('login'))
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('list_books'))
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

@permission_required('relationship_app.can_change_book', login_url=reverse_lazy('login'))
@login_required(login_url=reverse_lazy('login'))
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('list_books'))
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})

@permission_required('relationship_app.can_delete_book', login_url=reverse_lazy('login'))
@login_required(login_url=reverse_lazy('login'))
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(reverse_lazy('list_books'))
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})