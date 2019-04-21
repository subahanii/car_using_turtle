from django.shortcuts import render , redirect,HttpResponse
#from letsdo.forms import EmployeeForm
from letsdo.models import Employee


# Create your views here.
def index(request):

    if request.method=='POST':
        eid=request.POST.get('eid','')
        ename=request.POST.get('ename','')
        email=request.POST.get('email','')
        econtact=request.POST.get('econtact','')
        emp=Employee(eid=eid,ename=ename,econtact=econtact,email=email)
        emp.save()
        return redirect("/show")




    return render(request,"index.html")

def login(request,id=0,msg=''):
    print('id', id)
    if msg!='':
        return render(request, "login.html",{'msg':msg})

    if id==1:
        em=request.POST.get('email','')
        ep=request.POST.get('epass','')
        if em!='':
            try:
                employee = Employee.objects.get(email=em)

                if employee.email==em and employee.epass==ep:
                    request.session['username'] = em
                    print("login")
                    return redirect("/show")
                else:
                    print("else login")
                    return redirect("/login")
            except:
                print("exception")
                return redirect("/login")
        else:
            print("else em!=")
            return render(request,"login.html")

    return render(request,"login.html")




def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return redirect("/")


def register(request,id=0):
    if id==1:
        print(id)
        if request.method == 'POST':
            eid = request.POST.get('eid', '')
            ename = request.POST.get('ename', '')
            email = request.POST.get('email', '')
            epass = request.POST.get('epass', '')
            econtact = request.POST.get('econtact', '')
            emp = Employee(eid=eid, ename=ename, econtact=econtact, email=email, epass=epass)
            emp.save()
            return redirect("/login")

    return render(request,"register.html")


def show(request,uname=''):
    employees=Employee.objects.all()
    print(employees)

    if request.session.has_key('username'):
        uname = request.session['username']
        return render(request,"show.html",{'employees':employees,'uname':uname})
    else:
        return redirect("/")


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,"edit.html",{'employee' : employee } )


def update(request, id):
    employee = Employee.objects.get(id=id)

    employee.eid = request.POST.get('eid', '')
    employee.ename= request.POST.get('ename', '')
    employee.email = request.POST.get('email', '')
    employee.econtact = request.POST.get('econtact', '')

    employee.save()
    return redirect("/show")


def delete(request, id):

    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")



