from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", views.home, name="home"),
    path("employees/", views.employees, name="employees"),
    path("add-new-employee/", views.add_employee, name="add-employee")
]
