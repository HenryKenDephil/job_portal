from django.db import models
from django.contrib.auth.models import  User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from recruiters.models import Job



CHOICES = {
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote')
}


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    full_name = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(null=True, blank=True, max_length=255)
    location = models.CharField(null=True, blank=True, max_length=255)
    resume = models.FileField(upload_to='resumes')
    grad_year = models.IntegerField(blank=True)
    looking_for = models.CharField(null=True, max_length=30,  choices=CHOICES,
                                   default='Full Timme')
    slug = AutoSlugField(populate_from = 'user', unique = True)


    def get_absolute_url(self):
        return "/profile/{}".format(self.slug)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username
    

class Skill(models.Model):
    skill = models.CharField(max_length = 255)
    user = models.ForeignKey(
        User, related_name = "skills", on_delete = models.CASCADE)
    

class SavedJobs(models.Model):
    Job = models.ForeignKey(
        Job, related_name = "saved_job", on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name = "saved", on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.job.title 
    

class AppliedJobs(models.Model):
    job = models.ForeignKey(
        Job, related_name = "applied_job", on_delete = models.CASCADE)
    user = models.ForeignKey(
        User, related_name = "applied_user", on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.job.title


    


