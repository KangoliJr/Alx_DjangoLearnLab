from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# from .models import User
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title" ,"author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year")
    
admin.site.register(Book)



class UserAdmin(DefaultUserAdmin):
    pass

admin.site.register(CustomUser, UserAdmin)