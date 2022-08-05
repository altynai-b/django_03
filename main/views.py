from django.shortcuts import render
from django.http import HttpResponse

from .models import (
    Student,
)

def home(request):
    student = Student.objects.all()
    context = {
        'students': student
    }
    return render(request, 'main/home.html', context)

def index(request):
    return HttpResponse('<h1>Welcome to Index page!!!</h1>')