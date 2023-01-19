from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import AccessLog, Project
from .forms import ProjectForm

def index(request):
    project_list = Project.objects.order_by('date_proposed')[:20]
    context = {'project_list': project_list}
    return render(request, 'projects/index.html', context)

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

def delete_project(request):
    return 

def success(request):
    return HttpResponseRedirect('/projects')

# Create your views here.
