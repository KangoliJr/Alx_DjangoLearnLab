from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')
        
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content',]
#         widgets = {
#         'tags': TagWidget(attrs={'placeholder': 'Comma-separated tags ()'}),
#     }
        
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['content']
#         labels = {'content': 'Your Comment'}
#         widgets = {
#             'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}),
#         }
        
#     widgets = {
#         'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}),
#     }
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Comma-separated tags ()'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Your Comment'}
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}),
        }