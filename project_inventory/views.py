from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessLog

def index(request):
    log = AccessLog(access_count = 1)
    log.save()
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
