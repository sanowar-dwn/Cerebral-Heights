from django.shortcuts import render
from .models import Employee
# Create your views here.

def employee_all(request):
    return render(request, 'employee-all.html')


def employee_details(request, id):
    employee = Employee.objects.get(id=id)
    context = {
        'employee':employee
    }
    return render(request, 'employee-details.html', context)