from django.contrib import admin
from .models import Company, User, Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Company)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
