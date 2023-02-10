from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import IndustryPartnersForm
from .models import IndustryPartners

# Create your views here.
def add_industry_partner(request):
    # return render(request, 'projects/add.html')
    form = IndustryPartnersForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("Success")
            form.save()
            return redirect('contacts:success')

    return render(request, 'contacts/add.html', {'form': form})

def list(request):
    partners_list = IndustryPartners.objects.order_by('name')[:20]
    context = {'industry_partners_list': partners_list}
    return render(request, 'contacts/list.html', context)

def success(request):
    return HttpResponseRedirect('/contacts/list/')