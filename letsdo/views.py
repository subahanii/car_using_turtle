from django.shortcuts import render , redirect
from letsdo.forms import EmployeeForm
from letsdo.models import Employee


# Create your views here.
def emp(request):
    if request.method == "GET":
        print("djjd------------------------==========")
        form = EmployeeForm(request.GET)

        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass


    else:
        form = EmployeeForm()
    return render(request,"index.html",{'form':form})

def show(request):
    employees=Employee.objects.all()
    print(employees)
    return render(request,"show.html",{'employees':employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,"edit.html",{'employee' : employee } )


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.GET, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,"edit.html", {'employee': employee })


def delete(request, id):
    print(id,"=================================")
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")



