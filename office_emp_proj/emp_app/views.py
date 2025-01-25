from django.shortcuts import render, HttpResponse
from .models import Employee
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = int(request.POST.get('salary','0')or 0)
        bonus = int(request.POST.get('bonus','0')or 0)
        phone = int(request.POST.get('phone','0')or 0)
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        hire_date = request.POST.get('hire_date')
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse(request, 'Employee added successfully')
    elif request.method == 'GET':
        return render(request, 'add_employ.html')
    else:
        return HttpResponse("An exception Occured ! Employee Has not Been Added")

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee remove success")
        except:
            return HttpResponse("Please enter valid employee id")

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_employ.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    return render(request, 'filter_empl.html')