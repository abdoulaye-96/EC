"""
    admin of the user app
"""
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
