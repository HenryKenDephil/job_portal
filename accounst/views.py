
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User 
from django.contrib.auth.forms import AuthenticationForm
# from . forms import CustomerSignUpForm
from users.models import StudentUser,  Recruiter
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.

def admin_login(request):
    return render(request, 'admin_login.html')

def admin_signup(request):
    return render(request, 'admin_signup.html')

def recruiter_login (request):
    error = " "
    if request.method == 'POST':
       username = request.POST['email'];
       password = request.POST['password1'];
       user = authenticate(username=username, password= password)
       if user:
            try:
               user1 = Recruiter.objects.get(user=user)
               if user1.type == 'recruiter' and user1.status!='pending':
                   login(request, user)
                   error="no"
               else:
                   error= "not"
            except:
               error = "yes"
       else:
           error = "yes"
    d = {'error': error} 
    return render(request, 'recruiter_login.html')

def recruiter_signup (request):
    error = " "
    if request.method == 'POST':
        fname = request.POST['first_name'];
        lname = request.POST['last_name'];
        email = request.POST['email'];
        password = request.POST['password1'];
        contact = request.POST['contact'];
        company_name = request.POST['company_name'];
      
        try:
          user=User.objects.create_user(first_name = fname, last_name = lname, email = email, password=password)
          Recruiter.objects.create(user=user, mobile=contact, company_name= company_name, stype= "recruiter", status = "pedding")
          error = "no"
        except:
            error = "yes" 
    d ={'error':error}
    return render(request, 'recruiter_signup.html' , d)

def user_login(request):
    error = " "
    if request.method == 'POST':
       username = request.POST['email'];
       password = request.POST['password1'];
       user = authenticate(username=username, password= password)
       if user:
            try:
               user1 = StudentUser.objects.get(user=user)
               if user1.type == 'student':
                   login(request, user)
                   error="no"
               else:
                   error= "yes"
            except:
               error = "yes"
       else:
           error = "yes"
    d = {'error': error}      
    return render(request, 'user_login.html', d)


def user_signup(request):
    error = " "
    if request.method == 'POST':
        fname = request.POST['first_name'];
        lname = request.POST['last_name'];
        email = request.POST['email'];
        contact = request.POST['contact'];
        password = request.POST['password1'];
        image = request.POST['image'];
        gender = request.POST['gender'];
        try:
          user=User.objects.create_user(first_name = fname, last_name = lname, email = email, password=password)
          StudentUser.objects.create(user=user, mobile=contact, contact=contact, image= image, gender= gender, stype= "student")
        
          error = "no"
        except:
            error = "yes" 
    d ={'error':error}  
    return render(request, 'user_signup.html', d)



def Logout(request):
    logout(request)
    return redirect("home")

def change_password(request):
    return render(request, 'admin_login.html')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user_home.html')
