from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomUserCreationForm
def homepage(request):
    return render(request, 'authentication/index.html')

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
    return render(request, 'authentication/login_register.html', {'page': page})

@login_required(login_url=loginUser)
def logoutUser(request):
    logout(request)
    return redirect('homepage')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('homepage')

    context = {'form': form, 'page': page}
    return render(request, 'authentication/login_register.html', context)

