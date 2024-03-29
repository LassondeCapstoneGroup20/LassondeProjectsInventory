from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django import forms

from .forms import CapstoneForm, AwardForm
from .models import Capstone, Award
from projects.views import login_required, loginUser

from projects.models import Project

# Create your views here.
@login_required(login_url=loginUser)
def add_edit_capstone(request, year = None):
    if year:
        cap = get_object_or_404(Capstone, starting_year = year)
        form = CapstoneForm(request.POST or None, instance = cap)
    else:
        form = CapstoneForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/capstones')
    return render(request, 'capstones/add.html', {'form': form})

@login_required(login_url=loginUser)
def list(request):
    cap_list = Capstone.objects.order_by('starting_year')
    context = {'capstone_list': cap_list}
    return render(request, 'capstones/list.html', context)

@login_required(login_url=loginUser)
def delete_capstone(request, year):
    cap = get_object_or_404(Capstone, starting_year=year)
    if request.method == "POST":
        cap.delete()
    return HttpResponseRedirect('/capstones')

@login_required(login_url=loginUser)
def details(request, year):
    projects = Project.objects.filter(capstone_year=year)
    cap = get_object_or_404(Capstone, starting_year=year)
    awards = Award.objects.filter(capstone=year)
    return render(request, 'capstones/detail.html', {'capstone': cap, 'projects':projects, 'awards':awards})

@login_required(login_url=loginUser)
def add_award(request, year, id=None):
    AwardForm.base_fields['project'] = forms.ModelChoiceField(
        queryset = Project.objects.filter(capstone_year = year),
        widget = forms.Select,
        required = True,
    )
    AwardForm.base_fields['capstone']=forms.IntegerField(
        initial=year
    )
    if id:
        award = get_object_or_404(Award, id=id)
        form = AwardForm(request.POST or None, instance = award)
    else:
        form = AwardForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            url = reverse('capstones:details', kwargs={'year': year})
            return HttpResponseRedirect(url)
    return render(request, 'capstones/add_award.html', {'form': form})

@login_required(login_url=loginUser)
def delete_award(request, year, id):
    award = get_object_or_404(Award, id=id)
    if request.method == "POST":
        award.delete()
        url = reverse('capstones:details', kwargs={'year': year})
        return HttpResponseRedirect(url)