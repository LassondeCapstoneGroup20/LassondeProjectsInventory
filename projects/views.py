from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import DisciplineForm, GoalForm, ProjectForm
from .filters import ProjectFilter
from .models import EngDiscipline, Project, UNGoals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from authentication.views import login_required, loginUser

@login_required(login_url=loginUser)
def project_index_page(request):
    return render(request, 'projects/index.html')

@login_required(login_url=loginUser)
def list(request):
    project_filter = ProjectFilter(request.GET, queryset = Project.objects.all())
    context = {'filter_form': project_filter.form, 'project_list': project_filter.qs[:20]}
    return render(request, 'projects/list.html', context)

@login_required(login_url=loginUser)
def detail(request, proj_id):
    proj = get_object_or_404(Project, id=proj_id)
    return render(request, 'projects/detail.html', {'proj': proj})

@login_required(login_url=loginUser)
def delete_project(request, proj_id):
    proj = get_object_or_404(Project, id = proj_id)
    if request.method == "POST":
        proj.delete()
    return HttpResponseRedirect('/projects/list/')
    #return render(request, 'projects/delete.html', {'proj': proj})

@login_required(login_url=loginUser)
def add_edit_project(request, proj_id = None):
    if proj_id:
        proj = get_object_or_404(Project, id = proj_id)
        form = ProjectForm(request.POST or None, instance = proj)
    else:
        form = ProjectForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects/list/')
    return render(request, 'projects/add.html', {'form': form})
    
@login_required(login_url=loginUser)
def settings(request):
    eng_disciplines = EngDiscipline.objects.order_by('id')[:15]
    un_goals = UNGoals.objects.order_by('id')[:18]
    context = {'disciplines': eng_disciplines, 'goals':un_goals}
    return render(request, 'projects/settings.html', context)

@login_required(login_url=loginUser)
def add_discipline(request):
    if request.method == "POST":
        return __save_form(DisciplineForm(request.POST), 'projects:settings')
    form = DisciplineForm()
    return render(request, 'projects/add_settings.html', {'form': form})

@login_required(login_url=loginUser)
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
