from django.shortcuts import render
from .models import Ecommerce

def ecommerce(request):
    return render(request,"application/template1.html")

def insertData(request):
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('email')
        print(name,number,email)
        query=Ecommerce(name=name,number=number,email=email)
        query.save()
    return render(request,"application/template1.html")    