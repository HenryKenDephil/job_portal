from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate
# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user_home.html')



