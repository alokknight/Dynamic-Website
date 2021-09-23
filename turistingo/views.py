from django.shortcuts import render
from turistingo.models import Turistingo
from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
# Create your views here.

def turindex(request):
    turs=Turistingo.objects.all()
    return render(request,'turindex.html', {'turs':turs} )

