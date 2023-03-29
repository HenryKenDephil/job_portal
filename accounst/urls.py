from django.urls import path
from. import views

urlpatterns = [
    # path('login/', views.login, name= 'Customer-login'),
    path('user_login/', views.user_login, name= 'user_login'),
    path('admin_login/', views.admin_login, name= 'admin_login'),
    path('recruiter_login/', views.recruiter_login, name= 'recruiter_login'),
    path('user_signup/', views.user_signup, name= 'user_signup'),
    path('admin_signup/', views.admin_signup, name= 'admin_signup'),
    path('recruiter_signup/', views.recruiter_signup, name= 'recruiter_signup'),
    path('Logout/', views.Logout, name= 'Logout'),

]