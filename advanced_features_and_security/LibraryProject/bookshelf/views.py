from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from django import forms 
from .forms import ExampleForm
# Create your views here.
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        
@login_required 
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') # Redirect to the book list after successful creation
    else:
        form = BookForm() # Display an empty form for GET requests
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Create'})

@login_required
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk) # Get the book object or return a 404 error
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book) # Populate form with submitted data and existing instance
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book) # Display form pre-filled with existing book data for GET requests
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Update'})

@login_required
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    # For GET request, display a confirmation page
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# exampleform
@login_required
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            print("Form is valid! Data:", form.cleaned_data)
            return redirect('form_success')
    else:
        form = ExampleForm() 
    
   
    return render(request, 'bookshelf/form_example.html', {'form': form})


