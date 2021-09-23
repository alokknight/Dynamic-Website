from django.shortcuts import render
from blog.models import Blog
from datetime import datetime
from django.contrib import messages
# Create your views here.
def blog(request):
    blogs=Blog.objects.all()
    return render(request,"blog.html",{'blogs':blogs})

