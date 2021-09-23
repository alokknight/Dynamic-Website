from django.shortcuts import render
from myprojects.models import Project

# Create your views here.
def projects(request):
    projects=Project.objects.all()
    return render(request, 'projects.html',{'projects':projects})