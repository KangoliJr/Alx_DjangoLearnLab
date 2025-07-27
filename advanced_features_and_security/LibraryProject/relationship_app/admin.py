from django.contrib import admin
from .models import UserProfile, CustomUser
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
# Register your models here.
admin.site.register(UserProfile)

class UserAdmin(DefaultUserAdmin):
    pass

admin.site.register(CustomUser, UserAdmin)