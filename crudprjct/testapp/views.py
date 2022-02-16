from django.shortcuts import render,redirect
from testapp.models import employee
from testapp.forms import EmployeeFrom

# Create your views here.
def retrive_view(request):
    emp_lsit=employee.objects.all()
    return render (request,'testapp/home.html',{'emp_list':emp_lsit})

def insert_view(request):
    form=EmployeeFrom()
    if request.method=='POST':
        form=EmployeeFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'testapp/insert.html',{'form':form})

def delete_view(request,id):
    Employee=employee.objects.get(id=id)
    Employee.delete()
    return redirect('/')

def update_view(request,id):
    Employee=employee.objects.get(id=id)
    form = EmployeeFrom(instance = Employee) #populate form with emp data
    if request.method == 'POST':
        form = EmployeeFrom(request.POST,instance=Employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})



