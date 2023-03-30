from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recruiter(models.Model):
    company_name = models.CharField(max_length= 200, unique=True, db_index=True),
    email = models.EmailField(max_length= 60),
    mobile = models.CharField(max_length= 15),
    password = models.CharField(max_length= 15),
    country = models.CharField(max_length= 60),
    town = models.CharField(max_length= 60),
    address = models.CharField(max_length= 60),
    date_joined = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.type

# class Applicant(models.Model):
#     user = models.ForeignKey( User, null=True , max_length=20, on_delete=models.CASCADE )
#     fname = models.CharField(max_length= 20, null=True  ),
#     lname = models.CharField(max_length= 20 ,null=True  ),
#     email = models.EmailField(max_length= 250, null=True ,help_text='e.g youremail@gmail.com')
#     phone = models.CharField(max_length= 15 , null=True),
#     profile_picture = models.ImageField(null=True, blank=True),
    
#     def __str__(self):
#         return self.user.username

class StudentUser(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE )
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        return self.user.username


   