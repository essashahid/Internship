from django.db import models
from .user_profile import UserProfile

class Teacher(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE,related_name='teachers')
    name = models.CharField(max_length=100)
