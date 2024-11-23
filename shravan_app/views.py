from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from . models import *
# Create your views here.
def index(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def invoice(request):
    return render(request,'invoice.html')

def register(request):
    if request.method=="POST":
        first_n=request.POST.get("fname",None)
        last_n=request.POST.get("lname",None)
        email_n=request.POST.get("email",None)
        password_n=request.POST.get("password",None)

        user = User.objects.create_user(username=email_n,email=email_n,first_name=first_n,last_name=last_n,password=password_n)
        return redirect("login")
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username=request.POST.get("email")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)
        print(user)
        if not user:
            print("user not found please register")
        else:
            print("user found ,logged in")
            auth_login(request,user)
            print(request.user)
        return redirect("invoice")
    return render(request,"login.html")
    

def create_invoice(request):
    if request.method == "POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        invoice_date=request.POST.get("invoice_date")
        invoice_number=request.POST.get("invoice_number")
        state=request.POST.get("state")
        Invoice.objects.create(username=username,email=email,invoice_date=invoice_date,invoice_number=invoice_number,state=state,user=request.user)
    
    return render(request,"invoice.html")

def viewinvoice(request):
    invoices=Invoice.objects.all()
    context={"invoice1":invoices}
    print(invoices.first())

    return render(request,"viewinvoice.html",context)

def deleteinvoice(request,pk):
    Invoice.objects.filter(id=pk).delete()
    invoices=Invoice.objects.all()
    context={"invoice1":invoices}

    return render(request,"viewinvoice.html",context)
    
       
    