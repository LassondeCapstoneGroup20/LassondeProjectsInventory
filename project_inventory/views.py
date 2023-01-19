from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessLog, Project

def index(request):
    #log = AccessLog(access_count = 1)
    #log.save()
    #return HttpResponse("Hello, world. You're at the polls index.")
    project_list = Project.objects.order_by('date_proposed')[:10]
    context = {'project_list': project_list}
    return render(request, 'project_inventory/index.html', context)
    

# Create your views here.
