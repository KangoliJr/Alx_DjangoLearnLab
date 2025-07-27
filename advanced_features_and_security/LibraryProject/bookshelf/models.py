from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
def __str__(self):
    return f"{self.title} by {self.author}, ({self.publication_year})"


# advanced features
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
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
        