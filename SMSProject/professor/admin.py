from django.contrib import admin
from .models import Professor
# Register your models here.
admin.site.site_header = "Professor Management System Admin"
admin.site.site_title = "Professor Management System Admin Portal" 
admin.site.register(Professor)
admin.site.index_title = "Welcome to Professor Management System Admin Portal"
