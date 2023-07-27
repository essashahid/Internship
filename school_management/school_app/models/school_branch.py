from django.db import models
from .user_profile import UserProfile
from .school import School

class SchoolBranch(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)
    admins = models.ManyToManyField(UserProfile, blank=True, related_name='admin_school_branches')
    branch_managers = models.ManyToManyField(UserProfile, blank=True, related_name='manager_school_branches')
