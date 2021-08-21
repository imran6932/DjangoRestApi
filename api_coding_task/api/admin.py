from django.contrib import admin
from .models import Student

#Register My model for admin panel access

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll', 'city']