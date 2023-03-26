from django.contrib import admin
from .models import Profile, SavedJobs, Skill, AppliedJobs

# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(AppliedJobs)
admin.site.register(SavedJobs)