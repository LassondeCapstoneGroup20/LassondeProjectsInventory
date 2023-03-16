from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FacultyForm
from .models import Faculty
from projects.views import login_required, loginUser

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
            return HttpResponseRedirect('/faculty/list/')
    return render(request, 'faculty/add.html', {'form': form})

@login_required(login_url=loginUser)
def list(request):
    faculty_list = Faculty.objects.order_by('id')
    context = {'faculty_list': faculty_list}
    return render(request, 'faculty/list.html', context)

@login_required(login_url=loginUser)
def delete_faculty(request, faculty_id):
    fac = get_object_or_404(Faculty, id=faculty_id)
    if request.method == "POST":
        fac.delete()
    return HttpResponseRedirect('/faculty/list/')