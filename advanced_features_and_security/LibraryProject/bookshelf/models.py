from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    class Meta:
        permissions =[
            ('can_view', 'can_view'),
            ('can_create', 'can_create'),
            ('can_delete', 'can_delete')
        ]
    
def __str__(self):
    return f"{self.title} by {self.author}, ({self.publication_year})"


# advanced features
# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(null=True, blank=True)
#     profile_photo = models.ImageField
    
# class CustomUserManager(BaseUserManager):
#     def create_user(self, date_of_birth, profile_photo):
#         if not profile_photo:
#             raise ValueError("Please add a Profile photo")
#         user = self.model(profile_photo=self.profile_photo(profile_photo))
#         user.set_date_of_birth(date_of_birth)
#         user.save(using=self.db)
        
#         return user
    
#     def create_superuser(self, date_of_birth, profile_photo):
#         user = self.create_user(date_of_birth,profile_photo)
        
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
        
#         return user
        
        
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        
        user = self.model(username=username, email=email, **extra_fields)
        
        if password:
            user.set_password(password)
        

        user.date_of_birth = date_of_birth
        user.profile_photo = profile_photo 
        

        user.save(using=self._db) 
        return user
    

    def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True) 

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, email, password, date_of_birth, profile_photo, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    

    objects = CustomUserManager()

    def __str__(self):
        return self.username