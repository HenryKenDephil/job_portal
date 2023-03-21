from django.urls import path
from. import views

urlpatterns = [
    # path('login/', views.login, name= 'Customer-login'),
    path('user_login/', views.user_login, name= 'user_login'),
    path('admin_login/', views.admin_login, name= 'admin_login'),
    path('user_signup/', views.user_signup, name= 'user_signup'),

]