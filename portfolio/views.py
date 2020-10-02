from django.shortcuts import render

from .models import Project

# Create your views here.
def homepage(request):
    project_obj = Project.objects.all()
    return render(request, 'homepage.html', {'projects':project_obj, 'headline':"Sweeti Chauhan's Portfolio"})
