from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ProjectForm
from .models import AccessLog, Project

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage/index.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
    return render(request, 'homepage/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url=loginUser)
def project_index_page(request):
    return render(request, 'projects/index.html')

@login_required(login_url=loginUser)
def list(request):
    project_list = Project.objects.order_by('date_proposed')[:20]
    context = {'project_list': project_list}
    return render(request, 'projects/list.html', context)

@login_required(login_url=loginUser)
def detail(request, proj_id):
    proj = get_object_or_404(Project, id=proj_id)
    return render(request, 'projects/detail.html', {'proj': proj})

@login_required(login_url=loginUser)
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

@login_required(login_url=loginUser)
def delete_project(request, proj_id):
    proj = get_object_or_404(Project, id = proj_id)
    if request.method == "DELETE":
        proj.delete()
    return redirect('projects:success')
    #return render(request, 'projects/delete.html', {'proj': proj})

def success(request):
    return HttpResponseRedirect('/projects/list/')

# Create your views here.
