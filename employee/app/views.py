from django.shortcuts import render
from .models import Employees
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, "home.html")

def employees(request):
    if "search" in request.GET:
        search = request.GET["search"]
        all_employees_list = Employees.objects.filter(
            Q(name__contains=search) | Q(phone__contains=search) |
            Q(email__contains=search) | Q(age__contains=search) |
            Q(status__contains=search) | Q(gender__contains=search)
        ).order_by(Lower("name"))
        if not all_employees_list:
            context = {"employee_not_found": True}
            return render(request, "employees.html", context)
    else:
        all_employees_list = Employees.objects.all().order_by(Lower("name"))
    
    paginator = Paginator(all_employees_list, 10)
    page = request.GET.get("page")
    all_employees = paginator.get_page(page)
    context = {"employees": all_employees}
    return render(request, "employees.html", context)

def add_employee(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        age = request.POST.get("age")
        position = request.POST.get("position")
        status = request.POST.get("status")
        gender = request.POST.get("gender")
        description = request.POST.get("note")

        if not name or not phone or not email or not age or not position or not status or not gender:
            messages.error(request, "Please fill out all the required fields correctly!")
            return render(request, "add-employee.html")


        
        if name and phone and email and age and position and status and gender or description:
            db = Employees()
            db.name = name
            db.phone = phone
            db.email = email
            db.age = age
            db.position = position
            db.status = status
            db.gender = gender
            db.note = description
            db.save()
            messages.success(request=request, message="Employee added successfully")
            return HttpResponseRedirect("/employees")
        
    else:
        return render(request, "add-employee.html")

