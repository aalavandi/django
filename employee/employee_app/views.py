from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def home(request):
    return HttpResponse("Welcome to the Employee Management System")

def employee(request):
    employees = Employee.objects.all()   # <-- use different variable name
    return render(request, 'index.html', {'employees': employees})
