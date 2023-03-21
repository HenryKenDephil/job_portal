
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
# from . forms import CustomerSignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# from django.core.files.storage import FileSystemStorage
# Create your views here.

def admin_login(request):
    return render(request, 'admin_login.html')
def user_login(request):
    return render(request, 'user_login.html')
def user_signup(request):
    return render(request, 'user_signup.html')
# def login(request):
#     if request.method == 'POST':
#         form= AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username = username)
#             pas = authenticate(password= password)
#             if user is not None and pas is not None:
#                 login(request, user, pas)
#                 return redirect('home')
#             else:
#                 return redirect('login')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form':form})
        
# def register(request):
#     if request.method == 'POST':
#         form = CustomerSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             signup_user = User.objects.get(username=username)
#             customer_group = Group.objects.get(name= 'Customer')
#             customer_group.user_set.add(signup_user)
#             return redirect("{% url 'login'%}")
#     else:
#          form = CustomerSignUpForm() 
#     return   render(request, 'register.html', {'form':form}) 

