from django.contrib import admin
from .models import Employees

# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "gender", "age", "registered_at"]
    search_fields = ["name", "phone", "email", "age", "position", "status", "gender"]
    list_filter = ["status", "gender"]
    list_per_page = 10

admin.site.register(Employees, EmployeesAdmin)