from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('user_home/', views.user_home, name= 'user_home'),
   
  
    
]
