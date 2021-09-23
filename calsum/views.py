from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def calculate(request):
    #return HttpResponse('hello world')
    val1=3
    return render(request,"calculate.html",{'name':'AAlok Patel','name2':val1})
#name should be same in views.py and in html file in {{jinja}} formate for putting dynamic value



def add(request):
    # val1=int(request.GET['num1'])
    # val2=int(request.GET['num2'])
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1 + val2
    res2=int(eval(request.POST['num3']))
    return render(request,'result.html' , {'result': res,'result2':res2 })

def showcal(request):
    #return HttpResponse("<h1>alok patel</h1>")
    return render(request,'resume.html')