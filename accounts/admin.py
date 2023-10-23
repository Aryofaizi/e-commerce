from django.contrib import admin
from .models import CustomUser

1
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_superuser"]
