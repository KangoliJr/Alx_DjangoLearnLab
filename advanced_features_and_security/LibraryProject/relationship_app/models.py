from django.db import models
from django.contrib.auth.models import User, AbstractUser,BaseUserManager
from django.db.models.signals import post_save 
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return self.title
    
    class Meta:
        permissions =[
            ('can_add_book', 'can_add_book'),
            ('can_change_book', 'can_change_book'),
            ('can_delete_book', 'can_delete_book'),
        ]
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='library')
    
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField( max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    ROLE_CHOICES=[
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
    
    def __str__(self):
        return f'{self.user.username} - {self.role}'
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
        
# advanced features
class CustomUser(AbstractUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField
    
class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo):
        if not profile_photo:
            raise ValueError("Please add a Profile photo")
        user = self.model(profile_photo=self.profile_photo(profile_photo))
        user.set_date_of_birth(date_of_birth)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self, date_of_birth, profile_photo):
        user = self.create_user(date_of_birth,profile_photo)
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
        
