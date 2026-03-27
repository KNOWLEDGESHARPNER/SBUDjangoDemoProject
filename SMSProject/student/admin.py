from django.contrib import admin

from .models import Student

# Register your models here.
admin.site.site_header = "Student Management System Admin"
admin.site.site_title = "Student Management System Admin Portal"
admin.site.register(Student)
admin.site.index_title = "Welcome to Student Management System Admin Portal"