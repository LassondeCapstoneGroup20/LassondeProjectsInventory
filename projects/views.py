from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import DisciplineForm, GoalForm, ProjectForm
from .models import EngDiscipline, Project, UNGoals

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
    #if request.method == "POST":   
    #    return __save_form(ProjectForm(request.POST), 'projects:success')
    form = ProjectForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('projects:success')
    return render(request, 'projects/add.html', {'form': form})

@login_required(login_url=loginUser)
def delete_project(request, proj_id):
    proj = get_object_or_404(Project, id = proj_id)
    if request.method == "POST":
        proj.delete()
    return redirect('projects:success')
    #return render(request, 'projects/delete.html', {'proj': proj})

#Todo: Might be able to combine with add_project, just check if an instance is sent
#search for editing form creates new instance
def edit_project(request, proj_id):
    proj = get_object_or_404(Project, id = proj_id)
    form = ProjectForm(request.POST or None, instance = proj)
    if request.method == "POST":
        #return __save_form(ProjectForm(request.POST, instance = proj), 'projects:success')
        if form.is_valid():
            form.save()
            return redirect('projects:success')
    return render(request, 'projects/add.html', {'form': form})

def success(request):
    return HttpResponseRedirect('/projects/list/')

def settings(request):
    eng_disciplines = EngDiscipline.objects.order_by('id')[:15]
    un_goals = UNGoals.objects.order_by('id')[:18]
    context = {'disciplines': eng_disciplines, 'goals':un_goals}
    return render(request, 'projects/settings.html', context)

def add_discipline(request):
    if request.method == "POST":
        return __save_form(DisciplineForm(request.POST), 'projects:settings')
    form = DisciplineForm()
    return render(request, 'projects/add_settings.html', {'form': form})

def add_goal(request):
    #return HttpResponse('Add Goal')
    if request.method == "POST":
        return __save_form(GoalForm(request.POST), 'projects:settings')
    form = GoalForm()
    return render(request, 'projects/add_settings.html', {'form': form})


'''Helper Methods'''
def __save_form(form, redir):
    if form.is_valid():
        print("Success")
        form.save()
        return redirect(redir)

# Create your views here.
