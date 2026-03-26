from django.http import HttpResponse
from django.shortcuts import render

from .models import Student

# Create your views here.
def home(request):
    return render(request,'student/home.html')


def register(request):
    if request.method=="POST":
        name=request.POST['sname']
        mob=request.POST['mob']
        email=request.POST['email']
        usn=request.POST['usn']
        college=request.POST['college']
        degree=request.POST['degree']
        branch=request.POST['branch']
        sem=request.POST['sem']

        #Logic to save the data in database can be added here
        stu_obj=Student(
            name=name,
            mob=mob,
            email=email,
            usn=usn,
            college=college,
            degree=degree,
            branch=branch,
            sem=sem
        )
        #ORM(Object Relational Mapping) methods to save the data in database
        stu_obj.save()
        
        return render(request,'student/display.html',
                      {'name':name,'mob':mob,'email':email,'usn':usn,
                       'college':college,'degree':degree,'branch':branch,'sem':sem})
    else:
        return render(request,'student/register.html')
    
def display(request):
    #Logic to fetch the students records from database 
    students=Student.objects.all()#fetching all records from Student table
    return render(request,'student/display.html',{'stu_objs':students})

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('pwd')
        if email=='abc@sbu.edu.in' and password=='sbu@123':
            return HttpResponse('<h1>Login Successfull!!!</h1>')
        else:
            return HttpResponse('<h1>Login Failure!!!</h1>')
    else:
        return render(request,'student/login.html')