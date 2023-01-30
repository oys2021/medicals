from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request,"health/index.html")

def about(request):
    return render(request,"health/about-us.html")

def contact(request):
    return render(request,"health/contact.html")


def doctors(request):
    return render(request,"health/doctors.html")

def department(request):
    return render(request,"health/department.html")