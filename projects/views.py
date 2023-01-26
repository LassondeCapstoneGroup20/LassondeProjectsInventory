from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ProjectForm
from .models import AccessLog, Project


def index(request):
    return render(request, 'projects/index.html')

def list(request):
    project_list = Project.objects.order_by('date_proposed')[:20]
    context = {'project_list': project_list}
    return render(request, 'projects/list.html', context)

def detail(request, proj_id):
    proj = get_object_or_404(Project, id=proj_id)
    return render(request, 'projects/detail.html', {'proj': proj})

def add_project(request):
    #return render(request, 'projects/add.html')
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            print("Success")
            form.save()
            return redirect('projects:success')       
    
    form = ProjectForm()
    return render(request, 'projects/add.html', {'form': form})

def delete_project(request, proj_id):
    proj = get_object_or_404(Project, id = proj_id)
    if request.method == "DELETE":
        proj.delete()
    return redirect('projects:success')
    #return render(request, 'projects/delete.html', {'proj': proj})

def success(request):
    return HttpResponseRedirect('/projects/list/')

# Create your views here.
