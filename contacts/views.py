from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import IndustryPartnersForm
from .models import IndustryPartners
from projects.views import login_required, loginUser

# Create your views here.

@login_required(login_url=loginUser)
def add_industry_partner(request):
    # return render(request, 'projects/add.html')
    form = IndustryPartnersForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("Success")
            form.save()
            return redirect('contacts:success')

    return render(request, 'contacts/add.html', {'form': form})

@login_required(login_url=loginUser)
def list(request):
    partners_list = IndustryPartners.objects.order_by('name')
    context = {'industry_partners_list': partners_list}
    return render(request, 'contacts/list.html', context)

@login_required(login_url=loginUser)
def delete_partner(request, partner_id):
    instance = get_object_or_404(IndustryPartners, id=partner_id)
    if request.method == "POST":
        instance.delete()
    return redirect('contacts:success')

def success(request):
    return HttpResponseRedirect('/contacts/list/')