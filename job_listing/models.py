from django.db import models

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

class Applicant(models.Model):
    fname = models.CharField(max_length= 20),
    lname = models.CharField(max_length= 20),
    email = models.CharField(max_length= 15),
    phone = models.CharField(max_length= 15),
    # resume = models.FieldFile(),
    profile_picture = models.ImageField(),