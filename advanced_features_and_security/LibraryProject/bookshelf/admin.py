from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# from .models import User
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title" ,"author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)
    
admin.site.register(Book, BookAdmin)



class CustomUserAdmin(DefaultUserAdmin):
    fieldsets = DefaultUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = DefaultUserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}), 
    )
    
    list_display = DefaultUserAdmin.list_display + ('date_of_birth', 'profile_photo',)


admin.site.register(CustomUser, CustomUserAdmin)