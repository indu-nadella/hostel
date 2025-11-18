from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from hostel.models import HostelPersonDetails,HostelFeeDetails,HostelMenu
from hostel.forms import person_details,fee_details,menu_details
# Create your views here.

def register(request):
    message=''
    if request.method=="POST":
        UserName=request.POST.get('username')
        UserEmail=request.POST.get('email')
        Password=request.POST.get('password')
        ConfirmPassword=request.POST.get('confirm_password')

        if Password!=ConfirmPassword:
            message='Passwords do not match'
        elif User.objects.filter(username=UserName).exists():
            message='Username already exists'
        elif User.objects.filter(email=UserEmail).exists():
            message='Email already exists'
        else:
            user = User.objects.create_user(username=UserName, email=UserEmail, password=Password)
            user.save()
            message='New User Created Successfully! Please Login'
            return redirect('login') 

    return render(request,'frontend/person_register.html',{'message':message})

def login_view(request):
    message=''
    if request.method=='POST':
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        user=authenticate(request,username=Username,password=Password)

        if user is not None:
            login(request,user)
            message='Login Successfull'
            return redirect('home')
        else:
            message='Invalid login details'
    return render(request,'frontend/person_login.html',{'message':message})

def home(request):
    return render(request,'frontend/home.html')

def add_person(request):
    if request.method=="POST":
        form=person_details(request.POST,request.FILES)
        if(form.is_valid()):
           form.save()
           return redirect('person')
        else:
           print(form.errors)
    else:
        form=person_details()
    return render(request,'frontend/add_person.html',{'form':form})

def view_person(request):
    data=HostelPersonDetails.objects.all()
    return render(request,'frontend/person_details.html',{'data':data})

def edit_person(request,id):
    data=HostelPersonDetails.objects.get(id=id)
    if request.method=="POST":
        form=person_details(request.POST,instance=data)
        if(form.is_valid()):
           form.save()
           return redirect('person')
    else:
        form=person_details()
    return render(request,'frontend/add_person.html',{'form':form})

def delete_person(request,id):
    data=HostelPersonDetails.objects.get(id=id)
    data=delete()
    return redirect('person')

def add_fee(request):
    if request.method=="POST":
        form=fee_details(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('fee')
        else:
            print(form.errors)
    else:
        form=fee_details()
    return render(request,'frontend/add_fee.html',{'form':form})

def view_fee(request):
    data=HostelFeeDetails.objects.all()
    return render(request,'frontend/fee_details.html',{'data':data})

def edit_fee(request,id):
    data=HostelFeeDetails.objects.get(id=id)
    if request.method=="POST":
        form=fee_details(request.POST,instance=data)
        if(form.is_valid()):
           form.save()
           return redirect('fee')
        else:
           print(form.errors)
    else:
        form=fee_details()
    return render(request,'frontend/add_fee.html',{'form':form})

def delete_fee(request,id):
    data=HostelFeeDetails.objects.get(id=id)
    data=delete()
    return redirect('fee')

def add_menu(request):
    if request.method=="POST":
        form=menu_details(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('menu')
        else:
            form=menu_details()
    else:
        form=menu_details()
    return render(request,'frontend/add_menu.html',{'form':form})

def view_menu(request):
    data=HostelMenu.objects.all()
    return render(request,'frontend/menu_details.html',{'data':data})

def edit_menu(request,id):
    data=HostelMenu.objects.get(id=id)
    if request.method=="POST":
        form=menu_details(request.POST,instance=data)
        if(form.is_valid()):
           form.save()
           return redirect('menu')
        else:
           print(form.errors)
    else:
        form=menu_details()
    return render(request,'frontend/add_menu.html',{'form':form})

def delete_menu(request,id):
    data=HostelMenu.objects.get(id=id)
    data=delete()
    return redirect('menu')