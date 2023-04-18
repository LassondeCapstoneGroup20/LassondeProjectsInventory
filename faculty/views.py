from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FacultyForm
from .filters import FacultyFilter
from .models import Faculty
from projects.views import login_required, loginUser
from projects.models import Project

# Create your views here.
@login_required(login_url=loginUser)
def add_edit_faculty(request, faculty_id = None):
    if faculty_id:
        fac = get_object_or_404(Faculty, id = faculty_id)
        form = FacultyForm(request.POST or None, instance = fac)
    else:
        form = FacultyForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/faculty')
    return render(request, 'faculty/add.html', {'form': form})

@login_required(login_url=loginUser)
def list(request):
    faculty_filter = FacultyFilter(request.GET, queryset = Faculty.objects.all())
    context = {'filter_form':faculty_filter.form, 'faculty_list': faculty_filter.qs}
    return render(request, 'faculty/list.html', context)

@login_required(login_url=loginUser)
def delete_faculty(request, faculty_id):
    fac = get_object_or_404(Faculty, id=faculty_id)
    if request.method == "POST":
        fac.delete()
    return HttpResponseRedirect('/faculty')

@login_required(login_url=loginUser)
def details(request, faculty_id):
    projects = Project.objects.filter(supervisor = faculty_id)
    faculty = get_object_or_404(Faculty, id=faculty_id)
    return render(request, 'faculty/detail.html', {'faculty': faculty, 'projects':projects})