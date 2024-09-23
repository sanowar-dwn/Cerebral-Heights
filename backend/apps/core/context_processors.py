from ..employee.models import Employee

def all_employees(request):
    return {'employee_all': Employee.objects.all()}