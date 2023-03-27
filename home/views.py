from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('accounst/user_login')
    return render(request, 'user_home.html')



