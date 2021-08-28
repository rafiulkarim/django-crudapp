from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee, Position

# Create your views here.
def employee_list(request):
    data = Employee.objects.all()
    position = Position.objects.all()
    context = {'data': data, 'position': position}
    return render(request, 'employee_register/employee_list.html', context)

def employee_form(request):
    data = Position.objects.all()
    context = {'data': data}
    return render(request, 'employee_register/employee_form.html', context)

def employee_register(request):
    if request.method == 'POST':
        employee = Employee()
        employee.fullname =  request.POST.get('fullname')
        employee.mobile =  request.POST.get('mobile')
        employee.emp_code =  request.POST.get('emp_code')
        employee.position_id =  request.POST.get('position')
        employee.save()
        return redirect('employee_list')
    else:
        return redirect('employee_form')

def employee_details(request, id):
    data = Employee.objects.filter(id=id)
    position = Position.objects.all()
    context = {'data': data, 'position': position}
    return render(request, 'employee_register/edit.html', context)

def employee_update(request, id):
    data = Employee.objects.get(pk=id)
    #return HttpResponse(data)
    data.fullname =  request.POST.get('fullname')
    data.mobile =  request.POST.get('mobile')
    data.emp_code =  request.POST.get('emp_code')
    data.position_id =  request.POST.get('position')
    data.save()
    #Employee.objects.get(id=id).update(fullname = request.POST.get('fullname'))
    return redirect('employee_list')
    
def employee_delete(request, id):
    Employee.objects.get(pk=id).delete()
    return redirect('employee_list')

def position(request):
    data = Position.objects.all()
    context = {'data': data}
    return render(request, 'employee_register/employee_form.html', context)


