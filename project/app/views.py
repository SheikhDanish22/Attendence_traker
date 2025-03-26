from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request,'home.html')



def login(request):
    Aemail='danish1521@gmail.com'
    Apass='danish'
    if request.method =='POST':
        user_email=request.POST.get('email')
        user_pass=request.POST.get('pass')
        
        
        x=staff.objects.filter(email=user_email)

        if user_email==Aemail and user_pass==Apass:
            return render(request,'admin.html')
        
        if x.exists():
            data=staff.objects.get(email=user_email)
            pass1=data.password
            if pass1==user_pass:
                return render(request,'user.html',{'name':data.name,'email':data.email})
            else :
                msg="Email id and Password doesnot match"
                return render(request,'home.html',{'msg':msg})
            
        else:
            msg2="Email id does not exits"
            return render(request,'home.html',{'msg2':msg2})

    return render(request,'home.html')    

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        branch=request.POST.get('pos')
        contact=request.POST.get('con')
        gender=request.POST.get('gender')
        
        
        user=staff.objects.filter(email=email)
        if user:
            return render(request,"addstaff.html",{'x':"email already exist"})
      
             

        else:
             staff.objects.create(
                name=name,
                email=email,
                gender=gender,
                branch=branch,
                
                contact=contact,
                
                )
             return render(request,"addstaff.html",{'y':'staff added successfully'})
    else:
             return render(request,'addstaff.html')
    
             
             
             
            
      


def display(request):
    mydata=staff.objects.all()
    
    return render(request,"display.html",{'myval':mydata})
    
def remove(request,pk):
    mydata=staff.objects.filter(id=pk)
    mydata.delete()

    myobj=staff.objects.all()
    
    return render(request,"display.html",{'myval':myobj})

def edit(request,pk):
    

    mydata=staff.objects.get(id=pk)
    
    return render(request,"edit.html",{"myval":mydata})
def update(request,pk):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        branch=request.POST.get('pos')
        contact=request.POST.get('con')
        gender=request.POST.get('gender')
        addtask=request.POST.get('task')
        
        x=staff.objects.get(id=pk)
        x.name=name
        x.email=email
        x.gender=gender
        x.branch=branch
        x.contact=contact
        
        x.save()
    mydata=staff.objects.all()
    return render(request,"display.html",{'myval':mydata})   

def addf(request,pk):
     mydata=staff.objects.get(id=pk)
     
def logout(request):
    return render(request,"home.html")

def attendence(request):
    mydata=staff.objects.all()
    return render(request,"attendence.html",{'myval':mydata})
def branch(request):
    if request.method=="POST":
     branch=request.POST.get("branch")
     mydata=staff.objects.filter(branch=branch)
     
     
     return render(request,"attendence.html",{'myval1':mydata})
    
def myattend(request):

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        branch=request.POST.get('branch')
    
        gender=request.POST.get('gender')
        date=request.POST.get("date")
        status=request.POST.get("status")
        print(name,email,branch,gender,date,status)

        Attendence.objects.create(
            name=name,
            email=email,
            branch=branch,
            gender=gender,
            date=date,
            
            status=status
        )
        
        mydata=staff.objects.filter(branch=branch)

        
    
    return render(request,"attendence.html",{'myval1':mydata})

def show(request):
    return render(request,"show.html")

def serch1(request):
    if request.method=='POST':
        name=request.POST.get("name")
        mydata=Attendence.objects.filter(
            Q(name__icontains=name)| Q(email__icontains=name)| Q(gender__icontains=name)| Q(status__icontains=name)| Q(branch__icontains=name)
        )

    return render(request,"show.html",{'myvalue':mydata})

def serch2(request):
     if request.method=='POST':
        name=request.POST.get("pos")
        
        
        mydata=Attendence.objects.filter(  Q(name__icontains=name)| Q(email__icontains=name)| Q(gender__icontains=name)| Q(status__icontains=name)| Q(branch__icontains=name))

     return render(request,"show.html",{'myvalue':mydata})
    
