from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):

    context={
        'variable':"this is sent"
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is my page")

def about(request):
     return render(request,'about.html')
    #return HttpResponse("this is my about page")

def contact(request):
    if request.method == "POST":
        email= request.POST.get('email')
        Name=request.POST.get('Name')
        LastName=request.POST.get("LastName")
     
        city=request.POST.get('city')
        contact=Contact( email=email,city=city,Name=Name,LastName=LastName,date=datetime.today())
        contact.save()

    return render(request,'contact.html')
   
def services(request):
     return render(request,'services.html')
    #return HttpResponse("this is my services page")

