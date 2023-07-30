from django.db import models
from .classroom import Classroom
from .user_profile import UserProfile

class Student(models.Model):
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE,related_name='students')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    
